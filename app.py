import streamlit as st

import os
import tempfile
from typing import Optional
from pydantic import BaseModel, Field, ValidationError
import streamlit as st

from form_extraction import  run_form_extraction_agent


def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        os.environ["OPENAI_API_KEY"] = "your_api_key_here"
          

    st.set_page_config(layout="wide")
    st.title("Einbürgerungsantrag Formular")

    file = st.file_uploader("Upload filled form (if any)", type=["pdf", "jpg", "png"])

    if file:
        file_content = file.read()
        response = run_form_extraction_agent(file_content)
        print(response.content)
        st.write("### Extracted Form Data:")
        content = response.content



    if file and response:
        col1,col2 = st.columns([0.3, 0.7])
        with col1:
            st.image(file_content)
        with col2:
            with st.form("einbuergerung_form"):
                # --- Personalien ---
                st.header("📝 Personalien")
                familienname = st.text_input("Familienname (ggf. Geburtsname)" , value= content.familienname)
                ggf_fruehere_namen = st.text_input("ggf. frühere Namen", value= content.ggf_fruehere_namen)
                vorname = st.text_input("Vorname(n)", value= content.vorname)
                geburtsdatum = st.text_input("Geburtsdatum (ISO-Format falls möglich)", value= content.geburtsdatum)

                geschlecht_m = st.checkbox("Geschlecht: männlich (m)" , value= content.geschlecht_m)
                geschlecht_w = st.checkbox("Geschlecht: weiblich (w)", value= content.geschlecht_w)
                geschlecht_d = st.checkbox("Geschlecht: divers (d)", value= content.geschlecht_d)

                geburtsort_land = st.text_input("Geburtsort, Land" , value= content.geburtsort_land)
                derzeitige_anschrift = st.text_area("Derzeitige Anschrift" , value= content.derzeitige_anschrift)
                telefon = st.text_input("Telefonnummer", value= content.telefon)
                e_mail = st.text_input("E-Mail-Adresse", value= content.e_mail)
                derzeitige_beschaeftigung = st.text_input("Derzeitige Beschäftigung", value= content.derzeitige_beschaeftigung)

                # --- Familienstand ---
                st.header("👪 Familienstand")
                familienstand_ledig = st.checkbox("ledig" , value= content.familienstand_ledig)
                familienstand_verheiratet = st.checkbox("verheiratet", value= content.familienstand_verheiratet)
                familienstand_eingetragene_lebenspartnerschaft = st.checkbox("eingetragene Lebenspartnerschaft", value= content.familienstand_eingetragene_lebenspartnerschaft)
                familienstand_verwitwet = st.checkbox("verwitwet", value= content.familienstand_verwitwet)
                familienstand_geschieden = st.checkbox("geschieden", value= content.familienstand_geschieden)
                familienstand_getrennt_lebend = st.checkbox("getrennt lebend", value= content.familienstand_getrennt_lebend)
                seit = st.text_input("Seit (wenn relevant)", value= content.seit)

                # --- Eheschließung ---
                st.header("💍 Eheschließung / Lebenspartnerschaft")
                datum_ehe_lebenspartnerschaft = st.text_input("Datum der Eheschließung / Lebenspartnerschaft", value= content.datum_ehe_lebenspartnerschaft)
                ort_land_ehe = st.text_input("Ort, Land der Eheschließung / Lebenspartnerschaft", value= content.ort_land_ehe)

                # --- Ausweispapiere ---
                st.header("🛂 Art der Ausweispapiere")
                auslaendischer_reisepass = st.checkbox("ausländischer Reisepass", value= content.auslaendischer_reisepass)
                auslaendischer_personalausweis = st.checkbox("ausländischer Personalausweis", value= content.auslaendischer_personalausweis)
                reiseausweis_oder_ausweilersatz = st.checkbox("Reiseausweis / Ausweilersatz der deutschen Ausländerbehörde", value= content.reiseausweis_oder_ausweilersatz)

                # --- Ausweisdetails ---
                st.subheader("📄 Ausweisdetails" )
                ausweis_nummer = st.text_input("Ausweis-Nummer", value= content.ausweis_nummer)
                ausstellungsbehoerde = st.text_input("Ausstellungsbehörde" , value= content.ausstellungsbehoerde)
                ausstellungsdatum = st.text_input("Ausstellungsdatum" , value= content.ausstellungsdatum)
                gueltigkeitsdatum = st.text_input("Gültigkeitsdatum" , value= content.gueltigkeitsdatum)

                # --- Submit ---
                submitted = st.form_submit_button("✅ Absenden")

                if submitted:
                    st.success("Formular erfolgreich abgesendet!")
                
if __name__ == "__main__":
    main()
