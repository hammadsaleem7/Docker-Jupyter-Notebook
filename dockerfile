# Dockerfile

# Use the official Jupyter Notebook base image
FROM jupyter/base-notebook:latest


# Expose the default Jupyter port
EXPOSE 8888

# Optionally, install additional Python packages
RUN pip install --no-cache-dir \
    numpy \
    pandas \
    matplotlib 
  

# Set the command to start Jupyter Notebook
CMD ["start-notebook.sh"]

