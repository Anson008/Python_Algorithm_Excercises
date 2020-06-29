def eval_reverse_polish_notation(tokens):
    if len(tokens) == 0:
        return 0
    st = []
    for i in range(len(tokens)):
        if tokens[i] == "+":
            r = st.pop()
            l = st.pop()
            st.append(l + r)
        elif tokens[i] == "-":
            r = st.pop()
            l = st.pop()
            st.append(l - r)
        elif tokens[i] == "*":
            r = st.pop()
            l = st.pop()
            st.append(l * r)
        elif tokens[i] == "/":
            r = st.pop()
            l = st.pop()
            st.append(r / l)
        else:
            st.append(int(tokens[i]))