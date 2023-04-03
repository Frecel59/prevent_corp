default:pytest

pytest:
	@echo "notest"

install:
	@pip install -r requirements.txt

streamlit:
	-@streamlit run api/app.py
