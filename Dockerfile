# Start with the official Nginx base image.
FROM nginx:latest

# Set the working directory inside the container.
WORKDIR /usr/share/nginx/html

# Remove the default Nginx index.html file.
RUN rm -f index.html

# Copy the static content of your website into the Nginx container.
# Assume that you have a directory 'static-website' containing your HTML, CSS, JavaScript, etc.
COPY . .

# Expose port 80 to the host so this container can serve traffic.
EXPOSE 80

# Start Nginx when the container has provisioned.
CMD ["nginx", "-g", "daemon off;"]