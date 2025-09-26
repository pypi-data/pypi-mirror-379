"""
CPF (Cadastro de Pessoa Física) processor.

Brazilian individual taxpayer registry document validation and formatting.
"""

from ...factories.document_factory import DocumentFactory

class CPF(DocumentFactory):
    
    def _format(self) -> str:
        doc_number=self._doc_number
        formatted = f'{doc_number[:3]}.{doc_number[3:6]}.{doc_number[6:9]}-{doc_number[9:]}'
        return formatted
    
    def _clean(self, doc_number:str) -> str:
        return ''.join(char for char in doc_number if char.isdigit())
    
    def _is_valid(self, doc_number:str) -> bool:
        # document lenght == 11
        if len(doc_number) != 11:
            self._error(f'CPF deve ter 11 digitos. Encontrados: {len(doc_number)}')
        
        # repeated numbers
        if len(set(doc_number)) == 1:
            self._error('CPF inválido: todos os dígitos são iguais')

        # check digit
        first_digit = self._calculate_digit(doc_number, 9)
        if first_digit != int(doc_number[9]):
            self._error('CPF inválido: primeiro dígito verificador incorreto')

        second_digit = self._calculate_digit(doc_number, 10)
        if second_digit != int(doc_number[10]):
            self._error('CPF inválido: segundo dígito verificador incorreto')
        
        return True
    
    def _calculate_digit(self, digits, position):
        total = 0
        for i in range(position):
            total += int(digits[i]) * (position + 1 - i)

        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder