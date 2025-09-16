
from typing import Optional
from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import List


class EinbuergerungsantragFormular(BaseModel):
    # --- Metadaten ---
    form_title: Optional[str] = Field(None, description="Titel des Formulars, z. B. 'Antrag auf Einbürgerung'")

    # --- Personalien der Antragstellerin / des Antragstellers ---
    familienname: Optional[str] = Field(None, description="Familienname, ggf. Geburtsname")
    ggf_fruehere_namen: Optional[str] = Field(None, description="ggf. frühere Namen")
    vorname: Optional[str] = Field(None, description="Vorname(n)")
    geburtsdatum: Optional[str] = Field(None, description="Geburtsdatum (wird auf ISO normalisiert, falls möglich)")
    geschlecht_m: bool = Field(False, description="Geschlecht männlich (m) ausgewählt")
    geschlecht_w: bool = Field(False, description="Geschlecht weiblich (w) ausgewählt")
    geschlecht_d: bool = Field(False, description="Geschlecht divers (d) ausgewählt")
    geburtsort_land: Optional[str] = Field(None, description="Geburtsort, Land")
    derzeitige_anschrift: Optional[str] = Field(None, description="Derzeitige Anschrift")
    telefon: Optional[str] = Field(None, description="Telefonnummer")
    e_mail: Optional[str] = Field(None, description="E-Mail-Adresse")
    derzeitige_beschaeftigung: Optional[str] = Field(None, description="Derzeitige Beschäftigung")

    # --- Familienstand ---
    familienstand_ledig: bool = Field(False, description="Familienstand: ledig")
    familienstand_verheiratet: bool = Field(False, description="Familienstand: verheiratet")
    familienstand_eingetragene_lebenspartnerschaft: bool = Field(
        False, description="Familienstand: eingetragene Lebenspartnerschaft"
    )
    familienstand_verwitwet: bool = Field(False, description="Familienstand: verwitwet")
    familienstand_geschieden: bool = Field(False, description="Familienstand: geschieden")
    familienstand_getrennt_lebend: bool = Field(False, description="Familienstand: getrennt lebend")
    seit: Optional[str] = Field(None, description="Seit (wenn relevant für Familienstand)")

    # --- Eheschließung / eingetr. Lebenspartnerschaft ---
    datum_ehe_lebenspartnerschaft: Optional[str] = Field(
        None, description="Datum der Eheschließung / eingetragenen Lebenspartnerschaft"
    )
    ort_land_ehe: Optional[str] = Field(None, description="Ort, Land der Eheschließung / Lebenspartnerschaft")

    # --- Art der Ausweispapiere ---
    auslaendischer_reisepass: bool = Field(False, description="Ausgewählt: ausländischer Reisepass")
    auslaendischer_personalausweis: bool = Field(False, description="Ausgewählt: ausländischer Personalausweis")
    reiseausweis_oder_ausweilersatz: bool = Field(
        False, description="Ausgewählt: Reiseausweis / Ausweilersatz der deutschen Ausländerbehörde"
    )

    # --- Ausweisdetails ---
    ausweis_nummer: Optional[str] = Field(None, description="Ausweis-Nummer")
    ausstellungsbehoerde: Optional[str] = Field(None, description="Ausstellungsbehörde")
    ausstellungsdatum: Optional[str] = Field(None, description="Ausstellungsdatum")
    gueltigkeitsdatum: Optional[str] = Field(None, description="Gültigkeitsdatum")
