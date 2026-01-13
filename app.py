import streamlit as st
import pandas as pd

# --- CONFIGURATION ---
st.set_page_config(page_title="FUT 26 Sniper", page_icon="⚽", layout="centered")

# --- FONCTIONS ---
def calculate_profit(buy_price, sell_price):
    tax = sell_price * 0.05
    net_sell = sell_price - tax
    profit = net_sell - buy_price
    return int(profit), int(tax)

# URL des images (On utilise une base de données générique pour l'exemple)
# Note : Il faudra mettre les vrais ID des joueurs pour avoir leur photo exacte
def get_card_image(player_id):
    return f"https://cdn.futbin.com/content/fifa25/img/players/{player_id}.png"

# --- DONNÉES EN TEMPS RÉEL (Simulation Basée sur notre analyse) ---
# C'est ici que tu mettras à jour tes flips manuellement ou via ton scraper
data = [
    {
        "name": "Mateus Mané (TOTW)", 
        "id": 274456, # ID Exemple (à changer selon le vrai ID Futbin)
        "rating": 86, 
        "buy_price": 14500, 
        "sell_price": 18500,
        "type": "Snipe Immédiat",
        "reliability": "🔥 100%"
    },
    {
        "name": "Pavel Šulc (TOTW)", 
        "id": 268432, 
        "rating": 86, 
        "buy_price": 14250, 
        "sell_price": 18000,
        "type": "Snipe Immédiat",
        "reliability": "🔥 100%"
    },
    {
        "name": "Patrik Schick", 
        "id": 234236, 
        "rating": 88, 
        "buy_price": 7800, 
        "sell_price": 11000,
        "type": "Erreur de Prix",
        "reliability": "✅ Sûr"
    },
    {
        "name": "Georges (Fodder)", 
        "id": 245367, 
        "rating": 87, 
        "buy_price": 7500, 
        "sell_price": 9800,
        "type": "Fodder Flip",
        "reliability": "✅ Sûr"
    }
]

# --- INTERFACE VISUELLE ---
st.title("⚽ FUT 26 | BEST FLIPS")
st.markdown(f"🗓️ *Scan du 13/01/2026 - Vente < 1h*")

# Affichage des cartes
for player in data:
    profit, tax = calculate_profit(player['buy_price'], player['sell_price'])
    
    # Cadre visuel
    with st.container():
        st.markdown("---")
        col_img, col_info, col_math = st.columns([1, 2, 2])
        
        with col_img:
            # Affiche l'image du joueur (si ID valide) ou une icône
            try:
                st.image(get_card_image(player['id']), width=80)
            except:
                st.write("⚽")
        
        with col_info:
            st.subheader(f"{player['name']}")
            st.caption(f"Note: {player['rating']} | {player['type']}")
            st.write(f"Fiabilité : {player['reliability']}")
            
        with col_math:
            st.metric("🎯 PRIX ACHAT MAX", f"{player['buy_price']:,} cr")
            st.metric("💰 REVENTE (Lazy)", f"{player['sell_price']:,} cr")
            st.markdown(f"**Profit Net :** :green[+{profit} cr]")
            st.caption(f"Taxe EA (5%) : -{tax} cr")

# Bouton de rafraichissement
if st.button("🔄 Actualiser les prix"):
    st.rerun()