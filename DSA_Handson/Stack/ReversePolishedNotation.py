tokens=["2","1","+","3","*"]
st=[]
for ch in tokens:
    if ch not in['+','-','*','/']:
        st.append(int(ch))
    else:
        a=st.pop()
        b=st.pop()
        if ch=='+':
            st.append(b+a)
        elif ch=='-':
            st.append(b-a)
        elif ch=='*':
            st.append(b*a)
        else:
            st.append(int(b/a))
print(st[-1])