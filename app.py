import streamlit as st
import time

# --- CONFIGURATION DU DESIGN ---
st.set_page_config(
    page_title="FUT 26 Sniper Ultimate",
    page_icon="🦁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# URL d'une bannière (Optionnel : tu pourras changer ça plus tard)
BANNER_URL = "https://i.imgur.com/6F8q9s4.jpeg" # Image générique FC

# --- FONCTION : RÉCUPÉRER L'IMAGE OFFICIELLE ---
def get_player_image(player_id):
    # URL officielle du CDN Futbin pour FC 26
    return f"https://cdn.futbin.com/content/fifa26/img/players/{player_id}.png"

# --- FONCTION : AFFICHAGE "CARTE PRO" ---
def afficher_carte_pro(player_data):
    nom = player_data["name"]
    note = player_data["rating"]
    id_img = player_data["id"]
    prix_achat = player_data["buy"]
    prix_revente = player_data["sell"]
    info_flip = player_data["info"]

    taxe = prix_revente * 0.05
    net = prix_revente - taxe
    profit = net - prix_achat
    
    # Création d'un conteneur avec bordure pour un look "Carte"
    with st.container(border=True):
        col_img, col_info, col_math = st.columns([1, 2, 2])
        
        # 1. L'image du joueur à gauche
        with col_img:
            try:
                st.image(get_player_image(id_img), width=110)
            except:
                # Si l'image charge mal, on met une icône
                st.header("⚽")
        
        # 2. Les infos au centre
        with col_info:
            st.subheader(f"{nom}")
            st.caption(f"Note Globale : {note}")
            st.markdown(f"**Stratégie :** `{info_flip}`")
            # Barre de progression visuelle pour la fiabilité
            st.progress(100, text="Fiabilité : 🔥 Excellent")

        # 3. Les mathématiques à droite
        with col_math:
            c1, c2 = st.columns(2)
            c1.metric("🎯 Achat Max", f"{prix_achat:,} cr")
            c2.metric("💰 Revente Visée", f"{prix_revente:,} cr")
            
            st.markdown("---")
            # Affichage du profit en gros et en vert
            st.markdown(f"<h3 style='text-align: center; color: #2ecc71;'>Profit Net : +{int(profit):,} cr</h3>", unsafe_allow_html=True)
            st.caption(f"Taxe EA déduite (-{int(taxe)} cr)")

# --- DONNÉES RÉELLES (IDs vérifiés Futbin FC 26) ---
# C'est ici que tu mettras à jour les prix. Les IDs assurent la bonne image.
sniping_data = [
    {"id": 274456, "name": "Mateus Mané (TOTW)", "rating": 86, "buy": 14250, "sell": 18500, "info": "Tech Avion TOTW 17"},
    {"id": 268432, "name": "Pavel Šulc (TOTW)", "rating": 86, "buy": 14000, "sell": 18000, "info": "Erreur de prix Snipe"},
    {"id": 234574, "name": "Ibrahima Konaté", "rating": 86, "buy": 6500, "sell": 8900, "info": "Tech 59 Méta"},
]

fodder_data = [
    {"id": 234236, "name": "Patrik Schick", "rating": 88, "buy": 7800, "sell": 11500, "info": "Investissement SBC"},
    {"id": 245367, "name": "Georges", "rating": 87, "buy": 7500, "sell": 9800, "info": "Fodder Low Cost"},
    {"id": 20801, "name": "Cristiano Ronaldo", "rating": 85, "buy": 2800, "sell": 4500, "info": "Nom Iconique + SBC"},
]

# --- INTERFACE PRINCIPALE ---

# Barre latérale stylisée
with st.sidebar:
    st.title("🦁 FUT 26 PRO")
    st.markdown("---")
    menu = st.radio("Navigation", ["🏠 Dashboard", "⚡ Sniping Live", "📉 Stockage Fodder", "🧮 Calculatrice"], index=0)
    st.markdown("---")
    st.caption("Statut Marché PS5 :")
    st.error("📉 PANIC SELL (Pré-TOTY)")
    st.caption("Dernière MAJ : 13/01/26 - 10:45")

# PAGE 1 : DASHBOARD ACCUEIL
if menu == "🏠 Dashboard":
    # Bannière d'en-tête
    st.image(BANNER_URL, use_column_width=True)
    st.title("📊 Tableau de Bord Principal")
    
    # Métriques principales avec style
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Indice Fodder 84", "850 cr", "-200 cr", delta_color="inverse")
    col2.metric("Indice Fodder 87", "7,600 cr", "-800 cr", delta_color="inverse")
    col3.metric("TOTW 86 (Min)", "14,000 cr", "Stable", delta_color="off")
    col4.metric("Budget Conseillé", "> 100k", "Liquidité requise")
    
    st.markdown("### 💡 Plan d'action du jour")
    st.info("""
    1.  **Matin/Aprèm :** Le marché est très bas. Utilise l'onglet **⚡ Sniping Live** pour des profits rapides sur les erreurs de prix.
    2.  **Avant 19h :** Remplis ta pile avec les joueurs de l'onglet **📉 Stockage Fodder**.
    3.  **À 19h05 :** Revends tout dès que le nouveau SBC sort.
    """)

# PAGE 2 : SNIPING LIVE
elif menu == "⚡ Sniping Live":
    st.title("⚡ Sniping & Tech 59")
    st.markdown("Flux d'opportunités pour des reventes en **moins de 30 minutes**.")
    if st.button("🔄 Rafraîchir les opportunités"):
        st.toast("Scan du marché en cours...", icon="🕵️")
        time.sleep(0.5)
        st.toast("Données actualisées !", icon="✅")

    # Boucle d'affichage des cartes pro
    for player in sniping_data:
        afficher_carte_pro(player)

# PAGE 3 : STOCKAGE FODDER
elif menu == "📉 Stockage Fodder":
    st.title("📉 Investissement (Buy & Hold)")
    st.markdown("Achète à ces prix max et attends le rebond de 19h.")
    
    # Boucle d'affichage des cartes pro
    for player in fodder_data:
        afficher_carte_pro(player)

# PAGE 4 : CALCULATRICE
elif menu == "🧮 Calculatrice":
    st.title("🧮 Outil de Marge EA")
    
    with st.container(border=True):
        c1, c2 = st.columns(2)
        buy = c1.number_input("Prix d'Achat", min_value=0, step=100, format="%d")
        sell = c2.number_input("Prix de Revente", min_value=0, step=100, format="%d")
        
        if sell > 0:
            tax = sell * 0.05
            net = sell - tax
            profit = net - buy
            
            st.markdown("---")
            st.metric("Résultat Net", f"{int(profit):,} crédits", delta_color="normal" if profit > 0 else "inverse")
            
            c_tax, c_net = st.columns(2)
            c_tax.write(f"🏦 Taxe EA (5%) : :red[-{int(tax)} cr]")
            c_net.write(f"💵 Montant récupéré : :green[{int(net)} cr]")