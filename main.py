import streamlit as st
from pathlib import Path
from pdf_processor import PDFProcessor  

st.set_page_config(page_title='Incremental PDF Page Remover', layout='wide')

st.title('Incremental PDF Page Remover')
st.markdown("""
    Upload your PDF file and remove any redundant pages!
    Just drag and drop your file below and click the button to process it.
""")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Save the uploaded file into scripts/ folder
if uploaded_file:
    # Create the scripts directory if it doesn't exist
    scripts_dir = Path("scripts")
    scripts_dir.mkdir(exist_ok=True)

    # Save the uploaded file
    file_path = scripts_dir / uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    # Process the uploaded file
    processor = PDFProcessor(file_path)  
    processed_path = processor.create_pdf_without_redundancy()

    st.success(f"Processed script saved. Ready to download!")

    # Provide a download link for the processed PDF
    with open(processed_path, "rb") as f:
        st.download_button(
            label="Download Processed PDF",
            data=f,
            file_name=f"{processed_path.name}",
            mime="application/pdf"
        )

st.markdown("---")
st.markdown("Made with ❤️ by [Dennis Mustafić](https://github.com/dennismstfc)")  # Replace with your name and GitHub URL
