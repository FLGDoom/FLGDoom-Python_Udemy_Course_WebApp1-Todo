import streamlit as st
import modules.functions as functions

# das ganze script wird jedes mal neu ausgeführt wenn eine action gemacht
# also so was wie enter in der input_label drücken

st.session_state # ist ein dict, wo aktuelle sachen drin sind
todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

# meins kombiniert mit on change
def remove_todo():
    todos = functions.get_todos()
    for todo in todos:
        if st.session_state[todo] == True:
            todos.remove(todo)
            functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("This app is going to increase your productivity")
#sein
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)# , on_change=remove_todo
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
        

st.text_input(label="Enter a todo ",
              label_visibility="hidden",
              placeholder="Add new todo",
              on_change=add_todo,
              key="new_todo")

# mit pip freeze > requirements.txt,
#  erstellt man die requirements.txt !!!Wichtig