from app.models.models import User, Perfil, Veiculos, Checklist, ChecklistItem
from datetime import datetime



# Criar código único para cada checklist
def generate_checklist_code():
    today = datetime.now().strftime("%d%m%y")
    last_checklist = Checklist.query.order_by(Checklist.id.desc()).first()
    last_number = int(last_checklist.codigo.split("-")[-1]) + 1 if last_checklist else 1
    return f"CHK-{today}-{last_number:03d}"


print(generate_checklist_code())