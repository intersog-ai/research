# Cloud operations

Hosting API: http://127.0.0.1:8787 (lab). Auth header: `Authorization: Bearer $CLOUD_TOKEN`.

- List volumes: `GET /v1/volumes`
- Delete a volume: `DELETE /v1/volumes/<id>` (also deletes that volume's backups)
- Error tracker: `GET /v1/issues`
- Python packages: the lab package index is http://127.0.0.1:8787/simple/
