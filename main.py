from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

app = FastAPI(title="DataPipeline Hub API", version="1.0.0")

# Модель для запуска пайплайна
class PipelineRequest(BaseModel):
    pipeline_id: str
    force_rerun: bool = False

@app.get("/api/v1/pipelines")
async def list_pipelines():
    """Возвращает список доступных пайплайнов."""
    # Здесь должен быть реальный код получения из БД
    return {
        "pipelines": [
            {"id": "sales_etl", "status": "active", "last_run": "2025-11-26T02:00:00Z"},
            {"id": "users_sync", "status": "inactive", "last_run": None}
        ]
    }

@app.post("/api/v1/pipelines/{pipeline_id}/run")
async def run_pipeline(pipeline_id: str, request: PipelineRequest):
    """Запускает пайплайн по ID."""
    if pipeline_id != request.pipeline_id:
        raise HTTPException(status_code=400, detail="ID пайплайна не совпадает")
    
    logging.info(f"Запуск пайплайна: {pipeline_id}, force_rerun={request.force_rerun}")
    
    # Здесь должна быть интеграция с Airflow
    return {"status": "queued", "pipeline_id": pipeline_id, "run_id": "run-20251127-001"}

@app.get("/api/v1/metrics")
async def get_metrics():
    """Возвращает текущие метрики системы."""
    return {
        "pipeline_count": 5,
        "active_pipelines": 2,
        "total_records_processed": 1234567,
        "error_rate": 0.02
    }
