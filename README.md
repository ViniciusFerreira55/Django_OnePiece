Django_OnePiece
Projeto utilizando Django para fins acadêmicos

Exigências

Python
Django

Estrutura
O sistema tem como principal finalidade exibir informações sobre o anime One Piece.

Instrução

Clonar o repositório do projeto:
git clone https://github.com/joeltonken/Django_OnePiece

Criar o ambiente virtual
python -m venv venv

Ative o venv

# linux: 
source venv/bin/activate

# windows: 
.\vevn\Scripts\activate

Instale as dependências
pip install -r requirements.txt

Execute as migrações
./manage.py migrate

Rode a aplicação
./manage.py runserver
