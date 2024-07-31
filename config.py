import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'OoR7Seengahliu9Ohthoov2uigh7Gu2chieGeichehae5ChuLae6shei1fiepaShie4SahngahF1ci6ui8yeg3aed2quer5ahpeth3OhtheeL8ahcheiR8eghaiLiexa'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
