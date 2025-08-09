# Text-to-Visuals: Developer Guide

## Main Idea
Convert textual descriptions into visual representations using AI models.

## Features
- Text-to-visual (diagram/image) generation
- AWS Bedrock foundational model integration (via LangChain)
- Modular, extensible backend (LangChain, LangGraph, LangSmith)
- Customizable model parameters
- Clear separation of concerns

## Project Components
- **Core Engine**: Handles text processing, intent understanding, and IR generation
- **Model Interface**: Abstraction for Bedrock and other AI models (see `server/model_bedrock.py`)
- **Workflow Orchestration**: Managed by LangGraph and LangChain
- **Observability**: LangSmith for monitoring and debugging
- **CLI/GUI/Frontend**: User interaction layer

## Architecture
- Modular, component-based
- Model logic, workflow, and API are separated
- Easy to swap/upgrade models and orchestration logic
- Clear separation between input, processing, and output

## Workflow
1. User inputs text (via frontend)
2. Backend uses Bedrock (via LangChain) for intent understanding and IR generation
3. LangGraph orchestrates workflow: intent → visual type → IR → Mermaid
4. Output is rendered in the frontend

## Use Cases
- Creative art generation
- Rapid prototyping for design
- Educational visual aids

## Improvements
- Add more visual types and model support
- Enhance output quality and workflow flexibility
- Integrate more cloud APIs and observability tools

---
Refer to this guide for a quick overview and development reference.
