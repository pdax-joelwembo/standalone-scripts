FROM continuumio/miniconda3:4.5.11

RUN apt-get update -y; apt-get upgrade -y; apt-get install -y vim-tiny vim-athena ssh

COPY environment.yml environment.yml

RUN conda env create -f environment.yml
RUN echo "alias l='ls -lah'" >> ~/.bashrc
RUN echo "source activate connect" >> ~/.bashrc

# Setting these environmental variables is the functional equivalent of running 'source activate my-conda-env'
ENV CONDA_EXE /opt/conda/bin/conda
ENV CONDA_PREFIX /opt/conda/envs/connect
ENV CONDA_PYTHON_EXE /opt/conda/bin/python
ENV CONDA_PROMPT_MODIFIER (connect)
ENV CONDA_DEFAULT_ENV connect
ENV PATH /opt/conda/envs/connect/bin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin