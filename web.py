from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flowers4U - Online Flower Delivery</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  
  
  <style>
    .carousel-caption {
      background-color: rgba(0, 0, 0, 0.5);
      padding: 20px;
      border-radius: 10px;
    }
    .featured-product .card {
      transition: transform 0.3s;
    }
    .featured-product .card:hover {
      transform: translateY(-10px);
    }
    

  </style>
</head>
<body>

<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container">
    <a class="navbar-brand" href="#">
      <img src="logo.avif" alt="Flowers4U" height="100px">
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ml-auto">
        <li class="nav-item active">
          <a class="nav-link" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Shop</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Contact</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
<!--Carousel Indicator-->
<div id="carouselExampleIndicators" class="carousel slide" >
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
    </div>
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="image1.jpg" class="d-block w-100" alt="...">
        <div class="carousel-caption text-left">
            <h2>Welcome to Flowers4U</h2>
            <p class="lead">Your destination for beautiful flowers and gifts</p>
          </div>
      </div>
      <div class="carousel-item">
        <img src="image2.jpg" class="d-block w-100" alt="...">
        <div class="carousel-caption text-left">
            <h2>Express Your Love</h2>
            <p class="lead">Send flowers to your loved ones</p>
          </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
<!-- Products  -->
<section class="container mt-5 featured-product">
  <h2 class="text-center mb-4">Featured Products</h2>
  <div class="row">
    <div class="col-md-4 mb-4">
      <div class="card">
        <img src="red rosees.jpg" class="card-img-top" alt="Product 1">
        <div class="card-body">
          <h5 class="card-title">Red Roses Bouquet</h5>
          <p class="card-text">A classic choice to express love and passion.</p>
          <a href="#" class="btn btn-primary">View Details</a>
        </div>
      </div>
    </div>
    <div class="col-md-4 mb-4">
      <div class="card">
        <img src="tulip basket.jpg" class="card-img-top" alt="Product 2">
        <div class="card-body">
          <h5 class="card-title">Mixed Tulips Basket</h5>
          <p class="card-text">Brighten someone's day with vibrant tulips.</p>
          <a href="#" class="btn btn-primary">View Details</a>
        </div>
      </div>
    </div>
    <div class="col-md-4 mb-4">
      <div class="card">
        <img src="orchid.jpg" class="card-img-top" alt="Product 3">
        <div class="card-body">
          <h5 class="card-title">Orchid Plant</h5>
          <p class="card-text">Elegant and long-lasting orchids to adorn any space.</p>
          <a href="#" class="btn btn-primary">View Details</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!--Footer-->
<footer class="bg-dark text-white text-center py-3">
  <p>&copy; 2024 Flowers4U. All rights reserved.</p>
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>

'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()