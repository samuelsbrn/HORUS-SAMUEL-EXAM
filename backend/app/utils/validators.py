def validate_input(data, required_fields):
    """Mengecek apakah field yang dibutuhkan ada dan tidak kosong"""
    if not data:
        return False, "Data tidak ditemukan"
    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            return False, f"Field '{field}' wajib diisi"
    return True, "Valid"