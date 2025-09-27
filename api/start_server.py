#!/usr/bin/env python3
"""
Startup script for the Global Market Research API
Handles initialization, configuration, and server startup
"""

import os
import sys
import logging
import uvicorn
from pathlib import Path

# Add the api directory to Python path
api_dir = Path(__file__).parent
sys.path.insert(0, str(api_dir))

from config import settings

def setup_logging():
    """Configure logging for the application"""
    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL),
        format=settings.LOG_FORMAT,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('api.log') if not settings.DEBUG else logging.NullHandler()
        ]
    )

def check_dependencies():
    """Check if required dependencies are available"""
    try:
        import boto3
        import fastapi
        import uvicorn
        logging.info("✅ All required dependencies are available")
        return True
    except ImportError as e:
        logging.error(f"❌ Missing dependency: {e}")
        logging.error("Please run: pip install -r requirements.txt")
        return False

def check_aws_credentials():
    """Check AWS credentials and Bedrock access"""
    try:
        import boto3
        
        # Try to create Bedrock client
        bedrock_client = boto3.client('bedrock-runtime', region_name=settings.AWS_REGION)
        
        # Test connection (this will fail gracefully if no access)
        try:
            bedrock_client.list_foundation_models()
            logging.info("✅ AWS Bedrock access confirmed")
            return True
        except Exception as e:
            logging.warning(f"⚠️ Bedrock access limited, using mock mode: {str(e)}")
            return False
            
    except Exception as e:
        logging.warning(f"⚠️ AWS credentials not configured, using mock mode: {str(e)}")
        return False

def print_startup_info():
    """Print startup information"""
    print("\n" + "="*60)
    print("🌍 GLOBAL MARKET RESEARCH AGENTS API")
    print("="*60)
    print(f"🚀 Starting server on {settings.HOST}:{settings.PORT}")
    print(f"📖 API Documentation: http://{settings.HOST}:{settings.PORT}/docs")
    print(f"📚 ReDoc: http://{settings.HOST}:{settings.PORT}/redoc")
    print(f"🏥 Health Check: http://{settings.HOST}:{settings.PORT}/health")
    print(f"🌍 Countries Supported: 195+")
    print(f"🏭 Industries Supported: 25+")
    print(f"🔧 Debug Mode: {settings.DEBUG}")
    print(f"📊 Log Level: {settings.LOG_LEVEL}")
    print("="*60)
    
    print("\n💡 Example API Calls:")
    print(f"curl -H 'Authorization: Bearer demo_token_123' http://{settings.HOST}:{settings.PORT}/health")
    print(f"python client_example.py")
    print("\n🔑 Authentication: Use any token starting with 'demo_' for testing")
    print("="*60 + "\n")

def main():
    """Main startup function"""
    
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    logger.info("Starting Global Market Research API...")
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check AWS access
    aws_available = check_aws_credentials()
    if not aws_available:
        logger.info("🔄 Running in mock mode - all functionality available for demo")
    
    # Print startup information
    print_startup_info()
    
    # Import the FastAPI app
    try:
        from main import app
        logger.info("✅ FastAPI application loaded successfully")
    except Exception as e:
        logger.error(f"❌ Failed to load FastAPI application: {e}")
        sys.exit(1)
    
    # Start the server
    try:
        uvicorn.run(
            "main:app",
            host=settings.HOST,
            port=settings.PORT,
            reload=settings.DEBUG,
            log_level=settings.LOG_LEVEL.lower(),
            access_log=True
        )
    except KeyboardInterrupt:
        logger.info("🛑 Server stopped by user")
    except Exception as e:
        logger.error(f"❌ Server startup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()