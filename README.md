# Questcdn Scrapper

## Method to Execute the Script:

---

<details>
  <summary><h3>〣 Docker Method</h3></summary>

#### Install Docker

First, you need to install Docker on your local machine. You can download the appropriate version of Docker for your operating system from the [Docker website](https://www.docker.com/products/docker-desktop).

  <details>
  <summary><h4>〣 Direct run by pulling image from dockerhub</h3></summary>
    
#### Run the Docker container by running the following command:

  ```
  docker run -it jisan09/qcpi-scrapper
  ```
  </details>
  
  <details>
  <summary><h4>〣 Manually Build</h3></summary>
    
#### Clone the Primenumbers-Tech Repository

- Open a terminal window on your machine.

- Clone the Primenumbers-Tech repository by running the following command:

   ```
   git clone https://github.com/Jisan09/Primenumbers-Tech
   ```

#### Build and Run the Docker Container

- Navigate to the `Primenumbers-Tech` directory by running the following command:

   ```
   cd Primenumbers-Tech
   ```

- Build the Docker container by running the following command:

   ```
   docker build -t scrapper .
   ```

- Run the Docker container by running the following command:

   ```
   docker run -it scrapper
   ```
    </details>
  
</details>

---

<details>
  <summary><h3>〣 Manually Running </h3></summary>
  
- #### Clone the Primenumbers-Tech Repository

  - Open a terminal window on your machine.

  - Clone the Primenumbers-Tech repository by running the following command:

     ```
     git clone https://github.com/Jisan09/Primenumbers-Tech
     ```
  - Navigate to the `Primenumbers-Tech` directory by running the following command:

     ```
     cd Primenumbers-Tech
     ```
- #### Download google chrome & chromedriver in your machine
- #### Add the path of chrome & chromedriver in `scrapper.py` replacing `None` 
  https://github.com/Jisan09/Primenumbers-Tech/blob/8fbdd1b72ad234e39affe469ec72140800ab0667/scrapper.py#L8
  https://github.com/Jisan09/Primenumbers-Tech/blob/8fbdd1b72ad234e39affe469ec72140800ab0667/scrapper.py#L9
  
- #### Install pip requirement 
  ```
  pip3 install -r requirements.txt
  ```
- #### Run the Script
  ```
  python3 scrapper.py
  ```
</details>

---
