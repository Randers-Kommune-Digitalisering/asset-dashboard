import streamlit as st
import streamlit_antd_components as sac
import pandas as pd
from utils.database_connection import get_asset_db
import streamlit_shadcn_ui as ui

db_client = get_asset_db()


def get_computer_overview():

    col_1 = st.columns([1])[0]

    with col_1:
        content_tabs = sac.tabs([
            sac.TabsItem('Randers Kommune Computere', tag='Randers Kommune Computere'),
        ], color='dark', size='md', position='top', align='start', use_container_width=True)

    try:
        if 'computer_data' not in st.session_state:
            results = []
            with st.spinner('Loading data...'):
                query = """
                SELECT unitname, serienummer, primaryuser, afdeling, primaryfullname, devicelicense
                FROM capa
                """
                result = db_client.execute_sql(query)
                if result is not None:
                    results.append(pd.DataFrame(result, columns=['unitname', 'serienummer', 'primaryuser', 'afdeling', 'primaryfullname', 'devicelicense']))
                else:
                    st.error("Failed to fetch data from the Postgres DB.")
                    return

            if results:
                st.success("Data fetched successfully from DB.")
                st.session_state.computer_data = pd.concat(results, ignore_index=True)
            else:
                st.error("No data to display.")
                return

        data = st.session_state.computer_data

        if content_tabs == 'Randers Kommune Computere':
            afdeling_options = data['afdeling'].unique()
            selected_afdeling = st.selectbox('Vælg afdeling', afdeling_options, help='Vælg afdeling for at se computer detaljer')

            filtered_data = data[data['afdeling'] == selected_afdeling]

            computer_options = filtered_data['unitname'].unique()
            selected_computer = st.selectbox('Vælg computer', computer_options, help='Vælg UnitName for at se computer detaljer')

            computer_details = filtered_data[filtered_data['unitname'] == selected_computer].iloc[0]
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                ui.metric_card(title="Fulde Navn", content=str(computer_details['primaryfullname']), description="Fulde navn på ejer af computer")
            with col2:
                ui.metric_card(title="Serial Nummer", content=str(computer_details['serienummer']), description="Serienummer på computer")
            with col3:
                ui.metric_card(title="DQ Nummer", content=str(computer_details['primaryuser']), description="DQ Nummer på ejer af computer")
            with col4:
                device_license_status = "JA" if computer_details['devicelicense'] else "Nej"
                ui.metric_card(title="Device License", content=device_license_status, description="Enhed har licens" if device_license_status == "JA" else "Enhed har ikke licens")

    except Exception as e:
        st.error(f'An error occurred: {e}')
    finally:
        db_client.close_connection()
