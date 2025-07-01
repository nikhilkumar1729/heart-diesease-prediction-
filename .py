from typing import List, Optional
from datetime import date

class HeartDiseaseEntry:
    def __init__(
        self,
        disease_name: str,
        diagnosis_date: Optional[date] = None,
        notes: Optional[str] = None,
        status: Optional[str] = "Active",  # Active, Resolved, Unknown
    ):
        self.disease_name = disease_name
        self.diagnosis_date = diagnosis_date
        self.notes = notes
        self.status = status

    def __repr__(self):
        return (
            f"{self.disease_name} (Diagnosed: {self.diagnosis_date}, "
            f"Status: {self.status}, Notes: {self.notes})"
        )

class PatientHeartDiseaseProfile:
    COMMON_HEART_DISEASES = [
        "Coronary Artery Disease (CAD)",
        "Heart Failure (Congestive Heart Failure)",
        "Arrhythmia (Irregular Heartbeat)",
        "Congenital Heart Disease",
        "Valvular Heart Disease",
        "Cardiomyopathy",
        "Pericardial Disease (Pericarditis)",
        "Endocarditis",
        "Aortic Disease (Aneurysm, Dissection)",
        "Hypertensive Heart Disease",
        "Rheumatic Heart Disease",
        "Myocardial Infarction (Heart Attack)",
        "Pulmonary Heart Disease (Cor Pulmonale)",
        "Ischemic Heart Disease",
        "Other"
    ]

    def __init__(self):
        self.entries: List[HeartDiseaseEntry] = []

    def add_disease(
        self,
        disease_name: str,
        diagnosis_date: Optional[date] = None,
        notes: Optional[str] = None,
        status: Optional[str] = "Active",
    ):
        entry = HeartDiseaseEntry(disease_name, diagnosis_date, notes, status)
        self.entries.append(entry)

    def list_diseases(self):
        return self.entries

    def __repr__(self):
        return "\n".join(str(entry) for entry in self.entries)

# Example usage:
if __name__ == "__main__":
    profile = PatientHeartDiseaseProfile()
    profile.add_disease(
        "Coronary Artery Disease (CAD)",
        diagnosis_date=date(2022, 5, 10),
        notes="Stent placed in 2022",
        status="Active"
    )
    profile.add_disease(
        "Arrhythmia (Irregular Heartbeat)",
        diagnosis_date=date(2019, 8, 21),
        notes="On medication",
        status="Active"
    )
    print("Patient's Heart Diseases:")
    print(profile)
