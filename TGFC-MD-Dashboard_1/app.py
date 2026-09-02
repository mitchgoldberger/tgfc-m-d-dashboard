"""
TGFC - M&D Dashboard — live dashboard
Deployed on Streamlit Cloud. Data is embedded below; edit the ROWS list
(or swap in a CSV / live source) to update.
"""
import pandas as pd
import streamlit as st

st.set_page_config(page_title="TGFC - M&D Dashboard", page_icon="🛡️", layout="wide")

# ---- Data -------------------------------------------------------------------
COLUMNS = ["Date", "T", "TGFC PO", "NSI PO", "M&D REF", "Vendor", "Pickup Location",
           "Item Description", "Item #", "Customer", "Delivery Location",
           "P/U Date", "Del Date", "W/O Pick-Up", "Pounds"]

V, M, N = "Vendor Delivery", "M&D International", "Northstar Imports"
B30, BGO = "Beef Trim 30%", "Beef Trim GO 20-30%"

def r(date, t, tgfc, nsi, pk, desc, item, dloc, pu, dl, wo, lbs):
    return [date, t, tgfc, nsi, "", M, pk, desc, item, N, dloc, pu, dl, wo, lbs]

ROWS = [
    r("8/14/26","DLVD",302535,39114,V,B30,1438,"Chicago, IL","NA","8/24/26","8/24/26",40000),
    r("8/14/26","DLVD",302536,39115,V,B30,1438,"Chicago, IL","NA","8/24/26","8/24/26",32240.4),
    r("8/14/26","DLVD",302537,39116,V,B30,1438,"Chicago, IL","NA","8/24/26","8/24/26",31546),
    r("8/20/26","DLVD",302543,39174,V,B30,1438,"Chicago, IL","NA","8/28/26","8/24/26",40000),
    r("8/20/26","DLVD",302544,39175,V,B30,1438,"Chicago, IL","NA","8/28/26","8/24/26",40000),
    r("8/20/26","DLVD",302545,39176,V,B30,1438,"Chicago, IL","NA","8/28/26","8/24/26",33263.4),
    r("8/21/26","DLVD",302546,39177,V,B30,1438,"Chicago, IL","NA","8/31/26","8/24/26",40000),
    r("8/21/26","DLVD",302547,39178,V,B30,1438,"Chicago, IL","NA","8/31/26","8/24/26",40000),
    r("8/21/26","DLVD",302548,39179,V,B30,1438,"Chicago, IL","NA","8/31/26","8/24/26",40000),
    r("8/21/26","NA",302549,39170,"Omaha, NE",BGO,80476,"CPU","8/27/26","8/28/26","8/24/26",42152),
    r("8/21/26","NA",302550,39171,"Omaha, NE",BGO,80476,"CPU","8/28/26","8/28/26","8/24/26",41444),
    r("8/21/26","NA",302551,39172,"Omaha, NE",BGO,80476,"CPU","8/31/26","9/1/26","8/24/26",40000),
    r("8/21/26","NA",302552,39173,"Omaha, NE",BGO,80476,"CPU","8/31/26","9/1/26","8/24/26",40000),
    r("8/24/26","DLVD",302554,39180,V,B30,1438,"Chicago, IL","NA","9/1/26","8/31/26",40000),
    r("8/24/26","DLVD",302555,39181,V,B30,1438,"Chicago, IL","NA","9/1/26","8/31/26",40000),
    r("8/24/26","DLVD",302556,39182,V,B30,1438,"Chicago, IL","NA","9/1/26","8/31/26",40000),
    r("8/24/26","DLVD",302557,39183,V,B30,1438,"Chicago, IL","NA","9/2/26","8/31/26",40000),
    r("8/24/26","DLVD",302558,39184,V,B30,1438,"Chicago, IL","NA","9/2/26","8/31/26",40000),
    r("8/24/26","DLVD",302559,39185,V,B30,1438,"Chicago, IL","NA","9/2/26","8/31/26",40000),
    r("8/24/26","DLVD",302560,39186,V,B30,1438,"Chicago, IL","NA","9/3/26","8/31/26",40000),
    r("8/24/26","DLVD",302561,39187,V,B30,1438,"Chicago, IL","NA","9/3/26","8/31/26",40000),
    r("8/24/26","DLVD",302562,39188,V,B30,1438,"Chicago, IL","NA","9/3/26","8/31/26",40000),
    r("8/25/26","DLVD",302571,39189,V,B30,1438,"Chicago, IL","NA","8/28/26","8/24/26",39133),
    r("8/25/26","DLVD",302572,39190,V,B30,1438,"Chicago, IL","NA","8/28/26","8/24/26",40000),
    r("8/25/26","DLVD",302573,39191,V,B30,1438,"Chicago, IL","NA","8/31/26","8/31/26",39188),
    r("8/25/26","DLVD",302574,39192,V,B30,1438,"Chicago, IL","NA","8/31/26","8/31/26",39268),
]
df = pd.DataFrame(ROWS, columns=COLUMNS)

# ---- Style ------------------------------------------------------------------
st.markdown("""
<style>
  .block-container {padding-top: 2rem;}
  h1 {color:#0f2a4a;}
  [data-testid="stMetricValue"] {color:#0f2a4a;}
  [data-testid="stMetricLabel"] {font-weight:600;}
</style>
""", unsafe_allow_html=True)

st.title("🛡️ TGFC - M&D Dashboard")
st.caption("Third Generation Food Company · M&D International → Northstar Imports · Beef Trim")

# ---- Filters ----------------------------------------------------------------
with st.sidebar:
    st.header("Filters")
    items = st.multiselect("Item Description", sorted(df["Item Description"].unique()),
                           default=sorted(df["Item Description"].unique()))
    dests = st.multiselect("Delivery Location", sorted(df["Delivery Location"].unique()),
                           default=sorted(df["Delivery Location"].unique()))
    order_dates = st.multiselect("Order Date", sorted(df["Date"].unique()),
                                 default=sorted(df["Date"].unique()))

f = df[df["Item Description"].isin(items)
       & df["Delivery Location"].isin(dests)
       & df["Date"].isin(order_dates)]

# ---- KPIs -------------------------------------------------------------------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Loads", f"{len(f)}")
c2.metric("Total Pounds", f"{f['Pounds'].sum():,.0f}")
c3.metric("Beef Trim 30%", f"{(f['Item Description']==B30).sum()} loads")
c4.metric("Beef Trim GO 20-30%", f"{(f['Item Description']==BGO).sum()} loads")

# ---- Table ------------------------------------------------------------------
st.subheader("Purchase Orders")
st.dataframe(
    f, use_container_width=True, hide_index=True,
    column_config={
        "Pounds": st.column_config.NumberColumn("Pounds", format="%.1f"),
        "TGFC PO": st.column_config.NumberColumn("TGFC PO", format="%d"),
        "NSI PO": st.column_config.NumberColumn("NSI PO", format="%d"),
        "Item #": st.column_config.NumberColumn("Item #", format="%d"),
    },
)

# ---- Chart ------------------------------------------------------------------
st.subheader("Pounds by Delivery Date")
by_del = f.groupby("Del Date")["Pounds"].sum().sort_index()
st.bar_chart(by_del, color="#1d4e7e")

# ---- Download ---------------------------------------------------------------
st.download_button("⬇️ Download filtered CSV", f.to_csv(index=False).encode("utf-8"),
                   "tgfc_md_dashboard.csv", "text/csv")
