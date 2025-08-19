# simpan data user ke cloud Supabase
from supabase import create_client, Client
from typing import Dict

# Ganti dengan URL & Key dari Supabase project kamu
url: str = "https://fhevcuwegonmxcecdhdh.supabase.co"
key: str = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZoZXZjdXdlZ29ubXhjZWNkaGRoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTc1MjA4NTUsImV4cCI6MjA3MzA5Njg1NX0.AeI590GvskYIYnlZNiv233zkedt6EydOdYw3SY3Zy_U"
)


supabase: Client = create_client(url, key)


def insert_data(data: Dict[str, str]) -> bool:
    response = supabase.table("user").insert(data).execute()
    return True if response.data else False


def cek_data(data: Dict[str, str]) -> bool:
    response = (
        supabase.table("user")
        .select("name,email,password")
        .eq("password", data.password)
    )
    return True if response.data else False
