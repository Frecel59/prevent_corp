default:pytest

pytest:
	@echo "notest"

install:
	@pip install -r requirements.txt

run_api:
	@uvicorn app:app --reload
