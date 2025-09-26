from abc import ABCMeta, abstractmethod
from typing import Optional

class DocumentFactory(metaclass=ABCMeta):
    """
    Classe base abstrata para criação de documentos.
    
    Fornece funcionalidades comuns para validação, limpeza e formatação
    de diferentes tipos de documentos (CPF, CNPJ, etc.).
    """
    def __init__(self, doc_number:Optional[str]=None):
        self._doc_number=''
        doc_number=str(doc_number) if doc_number is not None else ''
        if doc_number:
            self.set(doc_number)

    def set(self, doc_number:Optional[str]) -> None:
        doc_number=str(doc_number) if doc_number is not None else ''
        if self.validate(doc_number):
            cleaned = self._clean(doc_number)
            self._doc_number=cleaned
    
    @property
    def get(self) -> str:
        return self._doc_number
    
    @property
    def formatted(self) -> str:
        if not self._doc_number:
            return ''
        return self._format()
    
    @property
    def is_empty(self) -> bool:
        return not bool(self._doc_number)
    
    def validate(self, doc_number:str) -> bool:
        if not doc_number or not doc_number.strip() or doc_number is None or doc_number=='': 
            self._error('Número do documento não pode ser vazio')
        
        cleaned = self._clean(doc_number)
        
        if not cleaned:
            self._error('Documento não contém dados válidos após limpeza')
        
        if not self._is_valid(cleaned):
            self._error(f'Documento inválido: {doc_number}')
            
        return True
    
    @property
    def document(self) -> str:
        return self.__class__.__name__
    
    def _error(self, message:str) -> None:
        raise ValueError(f'Document: {self._doc_number} | {message}')
    
    def __str__(self) -> str:
        return self.formatted
    
    def __repr__(self) -> str:
        return f'{self.document}({self._doc_number})'
       
    @abstractmethod
    def _format(self) -> str:
        pass
    
    @abstractmethod
    def _clean(self, doc_number:str) -> str:
        pass
    
    @abstractmethod
    def _is_valid(self, doc_number:str) -> bool:
        pass