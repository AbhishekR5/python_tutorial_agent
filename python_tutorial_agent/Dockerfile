# Base: Conda + Python
FROM continuumio/anaconda3

# Set working directory
WORKDIR /app

# Copy environment and install
COPY environment.yml .
RUN conda env create -f environment.yml

# Use the created environment by default
SHELL ["conda", "run", "-n", "python_tutorial_env", "/bin/bash", "-c"]

# Copy source code
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Start Streamlit
CMD ["conda", "run", "--no-capture-output", "-n", "python_tutorial_env", "streamlit", "run", "streamlit_app.py"]
