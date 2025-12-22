# First step: compilation - this step helps to reduce the image size
FROM alpine:latest as builder
RUN echo "checking files" > validate.txt

# Second step: takes the information from the builder to not use all the image in order to
# help with the performance
FROM nginx:alpine
COPY --from=builder validacion.txt /usr/share/nginx/html/status.txt
COPY index.html /usr/share/nginx/html/index.html
