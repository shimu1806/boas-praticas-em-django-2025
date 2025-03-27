Curso boas praticas django

- isolar Secret KEY. Utilizar a lib  python_dotenv para isolar credenciais. 
    Instale a lib python_dotenv
    crie .env e insira as credenciais
    em settings (ou qualquer outro lugar), "os" de "pathlib" e from dotenv import load_dotenv
    exemplo: em SECRET_KEY: str(os.getenv('SECRET_KEY'))

- Criar Project com "." e nome "setup/config/main/sejalaoqfor"

- Ao invés de escrever apenas o nome do app em setings, escrever o diretorio de apps dentro do app. Da seguinte forma:
        INSTALLED_APPS = [
        ...
        ...
        ...
        'learnCastellinaEv1.apps.Learncastellinaev1Config',     <-- desse jeito
        'learnCastellinaEv1',                                   <-- ao invés desse
    ]