from modulo_RepositorioProvincias import RepositorioProvincias
from vistaProvincias import ProvinciaView
from modulo_ControladorProvincias import ControladorProvincias
from ObjectEncoder import ObjectEncoder

def main():
    conn= ObjectEncoder('datos.json')
    repo= RepositorioProvincias(conn)
    vista= ProvinciaView()
    ctrl= ControladorProvincias(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()
  
if __name__ == "__main__":
    main()