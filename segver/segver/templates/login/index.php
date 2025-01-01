<!doctype html>
<html>
<head>
    <meta charset="utf-8"/>
    <meta name="description" content="Resumen del contenido de la página">   
    <title>Ingreso Calidad</title>
    <!--Seccion Bootstrap-->
    <link rel="stylesheet" href="../../static/librerias/bootstrap-5.0.2-dist/css/bootstrap.css">
    <script type="text/javascript" src="../../static/librerias/bootstrap-5.0.2-dist/js/bootstrap.js"></script>
    <link href='https://fonts.googleapis.com/css?family=Allerta Stencil' rel='stylesheet'>
    <!--Seccion Jquery-->
    <script type="text/javascript" src="../../static/librerias/jquery-3.6.4.js/jquery-3.6.4.js"></script>
    <!--Seccion Propia de calidad-->
    <link rel="stylesheet" href="../../static/login/css/index.css" type="text/css"/>
    <!--<script type="text/javascript" src="../../static/login/index.js"></script>-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>@import url('https://fonts.googleapis.com/css2?family=Agu+Display&family=Readex+Pro:wght@160..700&display=swap');
    </style>
</head>
<body>
<!--SECCION DE MODALES-->
<!-- Modal alertas-->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Alerta</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body" id="mextendido">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
<!-- Modal formulario preingreso-->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Alerta</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body" id="mextendido">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
<!--FIN SECCION DE MODALES-->
<section class="h-100 gradient-form" style="background-color: #eee;">
  <div class="container py-3 h-100">
    <div class="row d-flex justify-content-center align-items-center h-90">
      <div class="col-xl-10">
        <div class="card rounded-3 text-black" style="background-image: url('../../static/login/imagenes/fondosegver.jpg'); background-size: cover; background-repeat: no-repeat; background-position: center;">
          <div class="row g-0">
            <div class="col-lg-6" style="height: 500px;">
              <div class="card-body p-md-4 mx-md-4">

                <div class="text-center">
                  <!--SECCION DE MODALES-->
                  <img src="../../static/login/imagenes/logo2024.png" style="width: 185px;" alt="logo">
                  <h4 style="font-family: 'Agu Display';font-size: 38px">SEGUIMIENTO Y VERIFICACION</h4>
                </div>
                <form id="form_login" action="/calidad/login_calidad" method="POST">
                  {% csrf_token %}
                  <div class="form-outline mb-3" style="height: 30px;">
                    <label class="form-label" for="Empresa" style="float: left;">Frente:</label>
                    <input type="text" id="Empresa" name="Empresa" class="form-control" placeholder="Identificador de Frente"  style="width: 70%; float: right;" disabled/>
                  </div>
                  <div class="form-outline mb-3" style="height: 30px;">
                    <label class="form-label" for="Username" style="float: left;">Username:</label>
                    <input type="text" id="Username" name="Username" class="form-control" placeholder="Usuario"  style="width: 70%; float: right;" />
                  </div>
                  <div class="form-outline mb-3" style="height: 30px;">
                    <label class="form-label" for="Password" style="float: left;">Password:</label>
                    <input type="Password" id="Password" name="Password" class="form-control" placeholder="Password"  style="width: 70%; float: right;" />
                  </div>
                  <div class="form-outline mb-1">
                    <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3" id="Ingreso">Ingresar</button>
                    <a class="text-muted" href="">Olvido su Password?</a>
                  </div>
                  <div class="alert alert-primary" style="padding-top: 0; padding-bottom: 0" role="alert">
                    {{mextendido}}
                  </div>
                </form>
              </div>
            </div>
            <div class="col-lg-6 d-flex align-items-center">
              <div class="text-black px-3 py-4 p-md-5 mx-md-4">
                <h4 class="mb-4">Seguimiento y verificacion</h4>
                <p class="small mb-0">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                  exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</body>
</html>