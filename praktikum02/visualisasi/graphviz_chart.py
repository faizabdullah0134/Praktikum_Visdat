import streamlit as st
import graphviz as gv

st.title("Praktikum 2 - Graphviz Chart")
st.write("Kelompok 2:")
st.markdown("""
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254
- Alim Rifai - 0110122068
""")

st.graphviz_chart("""
digraph {
    "Training Data" -> "ML Algorithm"
    "ML Algorithm" -> "Model"
    "Model" -> "Result Forecasting"
    "New Data" -> "Model"
}
""")

graph = gv.Digraph()
graph.edge("Training Data", "ML Algorithm")
graph.edge("ML Algorithm", "Model")
graph.edge("Model", "Result Forecasting")
graph.edge("New Data", "Model")
st.graphviz_chart(graph)