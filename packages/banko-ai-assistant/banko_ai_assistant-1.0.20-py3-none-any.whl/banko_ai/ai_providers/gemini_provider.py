"""
Google Gemini AI provider implementation.

This module provides Google Vertex AI/Gemini integration for vector search and RAG responses.
"""

import os
import json
from typing import List, Dict, Any, Optional
from sentence_transformers import SentenceTransformer
from sqlalchemy import create_engine, text

try:
    from google.cloud import aiplatform
    from google.oauth2 import service_account
    import vertexai
    from vertexai.generative_models import GenerativeModel
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

from .base import AIProvider, SearchResult, RAGResponse, AIConnectionError, AIAuthenticationError


class GeminiProvider(AIProvider):
    """Google Gemini AI provider implementation."""
    
    def __init__(self, config: Dict[str, Any], cache_manager=None):
        """Initialize Gemini provider."""
        if not GEMINI_AVAILABLE:
            raise AIConnectionError("Google Cloud AI Platform not available. Install with: pip install google-cloud-aiplatform vertexai")
        
        self.cache_manager = cache_manager
        
        self.project_id = config.get("project_id") or os.getenv("GOOGLE_PROJECT_ID")
        self.location = config.get("location") or os.getenv("GOOGLE_LOCATION", "us-central1")
        self.model_name = config.get("model") or os.getenv("GOOGLE_MODEL", "gemini-1.5-pro")
        self.embedding_model = None
        self.db_engine = None
        self.vertex_client = None
        self.genai_client = None
        self.credentials = None
        self.use_vertex_ai = True  # Try Vertex AI first, fallback to Generative AI
        super().__init__(config)
    
    def _validate_config(self) -> None:
        """Validate Gemini configuration."""
        if not self.project_id:
            raise AIAuthenticationError("Google project ID is required")
        
        # Set up authentication from service account key file
        try:
            credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
            if credentials_path and os.path.exists(credentials_path):
                self.credentials = service_account.Credentials.from_service_account_file(credentials_path)
                print(f"✅ Loaded Google credentials from: {credentials_path}")
                
                # Try Vertex AI first
                try:
                    vertexai.init(
                        project=self.project_id, 
                        location=self.location, 
                        credentials=self.credentials
                    )
                    
                    # Create the generative model using the correct model name
                    model_name = self.model_name
                    if model_name == "gemini-1.5-pro":
                        model_name = "gemini-1.5-pro-001"
                    elif model_name == "gemini-1.5-flash":
                        model_name = "gemini-1.5-flash-001"
                    elif model_name == "gemini-1.0-pro":
                        model_name = "gemini-1.0-pro-001"
                        
                    self.vertex_client = GenerativeModel(model_name)
                    self.use_vertex_ai = True
                    print(f"✅ Initialized Vertex AI with project: {self.project_id}, location: {self.location}, model: {self.model_name}")
                    
                except Exception as vertex_error:
                    print(f"⚠️  Vertex AI initialization failed: {vertex_error}")
                    print("🔄 Falling back to Generative AI API...")
                    
                    # Fallback to Generative AI API
                    try:
                        # Check if there's a GOOGLE_API_KEY environment variable
                        api_key = os.getenv("GOOGLE_API_KEY")
                        if api_key:
                            genai.configure(api_key=api_key)
                            self.genai_client = genai.GenerativeModel(self.model_name)
                            self.use_vertex_ai = False
                            print(f"✅ Initialized Generative AI API with model: {self.model_name}")
                        else:
                            print("❌ No GOOGLE_API_KEY found for Generative AI API fallback")
                            raise AIConnectionError("Both Vertex AI and Generative AI API initialization failed - no API key")
                        
                    except Exception as genai_error:
                        print(f"❌ Generative AI API initialization failed: {genai_error}")
                        raise AIConnectionError(f"Failed to initialize both Vertex AI and Generative AI: {vertex_error}")
                        
            else:
                print("❌ No GOOGLE_APPLICATION_CREDENTIALS found")
                raise AIAuthenticationError("Google credentials are required")
                
        except Exception as e:
            if isinstance(e, (AIConnectionError, AIAuthenticationError)):
                raise
            raise AIConnectionError(f"Failed to initialize Gemini provider: {str(e)}")
    
    def get_default_model(self) -> str:
        """Get the default Gemini model."""
        return "gemini-1.5-pro"
    
    def get_available_models(self) -> List[str]:
        """Get available Gemini models."""
        return [
            "gemini-1.5-pro",
            "gemini-1.5-flash",
            "gemini-1.0-pro"
        ]
    
    def _get_embedding_model(self) -> SentenceTransformer:
        """Get or create the embedding model."""
        if self.embedding_model is None:
            try:
                # Use configurable embedding model from environment or default
                embedding_model_name = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
                self.embedding_model = SentenceTransformer(embedding_model_name)
            except Exception as e:
                raise AIConnectionError(f"Failed to load embedding model: {str(e)}")
        return self.embedding_model
    
    def _get_db_engine(self):
        """Get database engine."""
        if self.db_engine is None:
            database_url = os.getenv("DATABASE_URL", "cockroachdb://root@localhost:26257/defaultdb?sslmode=disable")
            try:
                self.db_engine = create_engine(database_url)
            except Exception as e:
                raise AIConnectionError(f"Failed to connect to database: {str(e)}")
        return self.db_engine
    
    def search_expenses(
        self, 
        query: str, 
        user_id: Optional[str] = None,
        limit: int = 10,
        threshold: float = 0.7
    ) -> List[SearchResult]:
        """Search for expenses using vector similarity."""
        try:
            # Generate query embedding
            embedding_model = self._get_embedding_model()
            query_embedding = embedding_model.encode([query])[0]
            
            # Convert to PostgreSQL vector format
            search_embedding = json.dumps(query_embedding.tolist())
            
            # Build SQL query
            sql = """
            SELECT 
                expense_id,
                user_id,
                description,
                merchant,
                expense_amount,
                expense_date,
                1 - (embedding <-> %s) as similarity_score
            FROM expenses
            WHERE 1 - (embedding <-> %s) > %s
            """
            
            params = [search_embedding, search_embedding, threshold]
            
            if user_id:
                sql += " AND user_id = %s"
                params.append(user_id)
            
            sql += " ORDER BY similarity_score DESC LIMIT %s"
            params.append(limit)
            
            # Execute query
            engine = self._get_db_engine()
            with engine.connect() as conn:
                result = conn.execute(text(sql), params)
                rows = result.fetchall()
            
            # Convert to SearchResult objects
            results = []
            for row in rows:
                results.append(SearchResult(
                    expense_id=str(row[0]),
                    user_id=str(row[1]),
                    description=row[2] or "",
                    merchant=row[3] or "",
                    amount=float(row[4]),
                    date=str(row[5]),
                    similarity_score=float(row[6]),
                    metadata={}
                ))
            
            return results
            
        except Exception as e:
            raise AIConnectionError(f"Search failed: {str(e)}")
    
    def generate_rag_response(
        self, 
        query: str, 
        context: List[SearchResult],
        user_id: Optional[str] = None,
        language: str = "en"
    ) -> RAGResponse:
        """Generate RAG response using Google Gemini."""
        try:
            print(f"\n🤖 GOOGLE GEMINI RAG (with caching):")
            print(f"1. Query: '{query[:60]}...'")
            
            # Check for cached response first
            if self.cache_manager:
                # Convert SearchResult objects to dict format for cache lookup
                search_results_dict = []
                for result in context:
                    search_results_dict.append({
                        'expense_id': result.expense_id,
                        'user_id': result.user_id,
                        'description': result.description,
                        'merchant': result.merchant,
                        'expense_amount': result.amount,
                        'expense_date': result.date,
                        'similarity_score': result.similarity_score,
                        'shopping_type': result.metadata.get('shopping_type'),
                        'payment_method': result.metadata.get('payment_method'),
                        'recurring': result.metadata.get('recurring'),
                        'tags': result.metadata.get('tags')
                    })
                
                cached_response = self.cache_manager.get_cached_response(
                    query, search_results_dict, "gemini"
                )
                if cached_response:
                    print(f"2. ✅ Response cache HIT! Returning cached response")
                    return RAGResponse(
                        response=cached_response,
                        sources=context,
                        metadata={
                            'provider': 'gemini',
                            'model': self.get_default_model(),
                            'user_id': user_id,
                            'language': language,
                            'cached': True
                        }
                    )
                print(f"2. ❌ Response cache MISS, generating fresh response")
            else:
                print(f"2. No cache manager available, generating fresh response")
            
            # Prepare context
            context_text = self._prepare_context(context)
            
            # Prepare the prompt
            prompt = f"""You are Banko, a financial assistant. Answer based on this expense data:

Q: {query}

Data:
{context_text}

Provide helpful insights with numbers, markdown formatting, and actionable advice."""
            
            # Generate response using either Vertex AI or Generative AI client
            if self.use_vertex_ai and self.vertex_client:
                from vertexai.generative_models import GenerationConfig
                
                generation_config = GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=1000,
                    top_p=0.9,
                    top_k=40
                )
                
                # Make the request with Vertex AI
                response = self.vertex_client.generate_content(
                    prompt,
                    generation_config=generation_config
                )
                
                # Extract response text
                if response and response.text:
                    ai_response = response.text
                else:
                    ai_response = "I apologize, but I couldn't generate a response at this time."
                    
            elif self.genai_client:
                # Use Generative AI API
                response = self.genai_client.generate_content(
                    prompt,
                    generation_config={
                        'temperature': 0.7,
                        'max_output_tokens': 1000,
                        'top_p': 0.9,
                        'top_k': 40
                    }
                )
                
                # Extract response text
                if response and response.text:
                    ai_response = response.text
                else:
                    ai_response = "I apologize, but I couldn't generate a response at this time."
            else:
                ai_response = "No Gemini client available."
            
            # Cache the response for future similar queries
            if self.cache_manager and ai_response:
                # Convert SearchResult objects to dict format for caching
                search_results_dict = []
                for result in context:
                    search_results_dict.append({
                        'expense_id': result.expense_id,
                        'user_id': result.user_id,
                        'description': result.description,
                        'merchant': result.merchant,
                        'expense_amount': result.amount,
                        'expense_date': result.date,
                        'similarity_score': result.similarity_score,
                        'shopping_type': result.metadata.get('shopping_type'),
                        'payment_method': result.metadata.get('payment_method'),
                        'recurring': result.metadata.get('recurring'),
                        'tags': result.metadata.get('tags')
                    })
                
                # Estimate token usage (rough approximation for Gemini)
                prompt_tokens = len(query.split()) * 1.3  # ~1.3 tokens per word
                response_tokens = len(ai_response.split()) * 1.3
                
                self.cache_manager.cache_response(
                    query, ai_response, search_results_dict, "gemini",
                    int(prompt_tokens), int(response_tokens)
                )
                print(f"3. ✅ Cached response (est. {int(prompt_tokens + response_tokens)} tokens)")
            
            return RAGResponse(
                response=ai_response,
                sources=context,
                metadata={
                    'provider': 'gemini',
                    "model": self.model_name,
                    "project_id": self.project_id,
                    "location": self.location,
                    "language": language,
                    'user_id': user_id,
                    'cached': False
                }
            )
            
        except Exception as e:
            raise AIConnectionError(f"RAG response generation failed: {str(e)}")
    
    def generate_embedding(self, text: str) -> List[float]:
        """Generate embedding for text."""
        try:
            embedding_model = self._get_embedding_model()
            embedding = embedding_model.encode([text])[0]
            return embedding.tolist()
        except Exception as e:
            raise AIConnectionError(f"Embedding generation failed: {str(e)}")
    
    def test_connection(self) -> bool:
        """Test Gemini connection."""
        try:
            # Test with a simple completion using the appropriate client
            if self.use_vertex_ai and self.vertex_client:
                from vertexai.generative_models import GenerationConfig
                
                generation_config = GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=5
                )
                
                response = self.vertex_client.generate_content(
                    "Hello",
                    generation_config=generation_config
                )
                
                return response and response.text is not None
                
            elif self.genai_client:
                response = self.genai_client.generate_content(
                    "Hello",
                    generation_config={
                        'temperature': 0.7,
                        'max_output_tokens': 5
                    }
                )
                
                return response and response.text is not None
            else:
                return False
                
        except Exception as e:
            print(f"❌ Gemini connection test failed: {str(e)}")
            return False
    
    def _prepare_context(self, context: List[SearchResult]) -> str:
        """Prepare context text from search results."""
        if not context:
            return "No relevant expense data found."
        
        context_parts = []
        for i, result in enumerate(context, 1):
            context_parts.append(
                f"• **{result.description}** at {result.merchant}: ${result.amount:.2f} "
                f"({result.date}) - similarity: {result.similarity_score:.3f}"
            )
        
        return "\n".join(context_parts)
