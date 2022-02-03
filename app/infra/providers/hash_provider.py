from passlib.context import CryptContext

pad_context = CryptContext(schemes=['bcrypt'])

#recebe dois paramêtros um texto e uma hash verifixca se o texto bate com a hash
def hash_verify(text, hashed_text):
    return pad_context.verify(text, hashed_text)

#converte um texto em hash
def get_hash(text):
    return pad_context.hash(text)

