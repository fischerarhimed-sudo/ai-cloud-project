# System Architecture

The application is a cloud-native AI text generation service.

## Components
- FastAPI application (Docker container)
- Hugging Face Inference API (AI model)
- Railway cloud platform (compute)
- GitHub (version control)
- Terraform (infrastructure as code)

## Flow
1. User sends prompt to API
2. Backend forwards request to Hugging Face
3. AI generates text
4. Response returned to user
