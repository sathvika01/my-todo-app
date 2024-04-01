import streamlit as st
import functions2

todos = functions2.get_todos( )

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions2.write_todos(todos)

st.title("My todo App")
st.subheader("This is my todo")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions2.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()



st.text_input(label="",placeholder="Add new todo....",
              on_change=add_todo, key ='new_todo')
st.session_state
