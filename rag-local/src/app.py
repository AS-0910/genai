import streamlit as st
from processUploadFile import FileProcessor
from query import Query
from llm import LLM

def main():
    with st.sidebar:
        st.set_page_config(page_title="RAG Question Answer", page_icon=":sidebar:", layout="wide")
        st.header("RAG Question Answer")
        upload_file = st.file_uploader("Upload a file", type=["pdf"], accept_multiple_files=False)

    process = st.button("Process")
    fileProcessor = FileProcessor()

    if process:
        if upload_file is not None:
            try:
                result = fileProcessor.process_and_add_uploaded_file(upload_file)
                st.write(result)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please upload a file to process.")

    # Question and Answer Area
    st.header("RAG Question Answer")
    prompt = st.text_area("**Ask a question related to your document:**")
    ask = st.button(
        "Ask",
    )

    if ask and prompt:
        ## return type is list of dicts with keys "documents", "metadatas", and "ids"
        query=Query()
        results = query.query_collection(prompt)
        context = results.get("documents")[0]
        relevant_text, relevant_text_ids = query.re_rank_results(prompt, context)

        llm = LLM()
        response = llm.call_llm(context=relevant_text, prompt=prompt)
        st.write_stream(response)

        with st.expander("See retrieved documents"):
            st.write(results)

        with st.expander("See most relevant document ids"):
            st.write(relevant_text_ids)
            st.write(relevant_text)


if __name__ == "__main__":
    main()
