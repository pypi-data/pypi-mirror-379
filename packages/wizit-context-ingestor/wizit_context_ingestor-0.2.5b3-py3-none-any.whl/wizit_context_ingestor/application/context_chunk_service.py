from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from ..data.prompts import CONTEXT_CHUNKS_IN_DOCUMENT_SYSTEM_PROMPT, ContextChunk
from typing import Dict, Any, Optional, List
from .interfaces import AiApplicationService, PersistenceService, RagChunker, EmbeddingsManager
import logging


logger = logging.getLogger(__name__)


class ContextChunksInDocumentService:
    """
    Service for chunking documents.
    """

    def __init__(
        self,
        ai_application_service: AiApplicationService,
        persistence_service: PersistenceService,
        rag_chunker: RagChunker,
        embeddings_manager: EmbeddingsManager,
        target_language: str = 'es'
    ):
        """
        Initialize the ChunkerService.
        """
        self.ai_application_service = ai_application_service
        self.persistence_service = persistence_service
        self.rag_chunker = rag_chunker
        self.embeddings_manager = embeddings_manager
        self.target_language = target_language
        self.embeddings_manager.init_vector_store()
        self.chat_model = self.ai_application_service.load_chat_model()

    def _retrieve_context_chunk_in_document(self, markdown_content: str, chunk: Document, chunk_metadata: Optional[Dict[str, Any]] = None) -> Document:
        """Retrieve context chunks in document."""
        try:
            chunk_output_parser = PydanticOutputParser(pydantic_object=ContextChunk)
            # Create the prompt template with image
            prompt = ChatPromptTemplate.from_messages([
                ("system", CONTEXT_CHUNKS_IN_DOCUMENT_SYSTEM_PROMPT),
                (
                    "human", [{
                        "type": "text",
                            "text": f"Generate context for the following chunk: <chunk>{chunk.page_content}</chunk>,  ensure all content chunks are generated in '{self.target_language}' language"
                    }]
                ),
            ]).partial(
                document_content=markdown_content,
                format_instructions=chunk_output_parser.get_format_instructions()
            )
            model_with_structured_output = self.chat_model.with_structured_output(ContextChunk)
            # Create the chain
            chain = prompt | model_with_structured_output
            # Process the image
            results = chain.invoke({})
            chunk.page_content = f"Context:{results.context}, Content:{chunk.page_content}"
            chunk.metadata["context"] = results.context
            if chunk_metadata:
                for key, value in chunk_metadata.items():
                    chunk.metadata[key] = value
            return chunk

        except Exception as e:
            logger.error(f"Failed to retrieve context chunks in document: {str(e)}")
            raise


    def retrieve_context_chunks_in_document(self, markdown_content: str, chunks: List[Document], chunks_metadata: Optional[Dict[str, Any]] = None) -> List[Document]:
        """Retrieve context chunks in document."""
        try:
            context_chunks = list(map(
                lambda chunk: self._retrieve_context_chunk_in_document(markdown_content, chunk, chunks_metadata),
                chunks
            ))
            return context_chunks
        except Exception as e:
            logger.error(f"Failed to retrieve context chunks in document: {str(e)}")
            raise

    def get_context_chunks_in_document(self, file_key: str, file_tags: dict = {}):
        """
        Get the context chunks in a document.
        """
        try:
            markdown_content = self.persistence_service.load_markdown_file_content(file_key)
            langchain_rag_document = Document(
                page_content=markdown_content,
                metadata={
                    "source": file_key
                }
            )
            logger.info(f"Document loaded:{file_key}")
            chunks = self.rag_chunker.gen_chunks_for_document(langchain_rag_document)
            logger.info(f"Chunks generated:{len(chunks)}")
            context_chunks = self.retrieve_context_chunks_in_document(markdown_content, chunks, file_tags)
            logger.info(f"Context chunks generated:{len(context_chunks)}")
            self.embeddings_manager.index_documents(context_chunks)
            return context_chunks
        except Exception as e:
            logger.error("Error get_context_chunks_in_document")
            raise e

    def delete_document_context_chunks(self, file_key: str):
        """
        Delete the context chunks in a document.
        """
        try:
            self.embeddings_manager.delete_documents_by_source_id(file_key)
        except Exception as e:
            logger.error(f"Error delete_document_context_chunks: {str(e)}")
            raise e
