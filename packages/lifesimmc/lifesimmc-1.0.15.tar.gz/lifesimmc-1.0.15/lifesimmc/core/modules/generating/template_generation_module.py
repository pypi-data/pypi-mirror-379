from phringe.util.grid import get_meshgrid

from lifesimmc.core.modules.base_module import BaseModule
from lifesimmc.core.resources.base_resource import BaseResource
from lifesimmc.core.resources.template_resource import TemplateResource


class TemplateGenerationModule(BaseModule):
    """Class representation of the template generation module to generate templates of planets with unit flux.

    Parameters
    ----------
    n_setup_in : str
        The name of the input configuration resource
    n_template_out : str
        The name of the output template resource collection
    fov : float
        The field of view for which to generate the templates in radians
    """

    def __init__(
            self,
            n_setup_in: str,
            n_template_out: str,
            fov: float
    ):
        """Constructor method.

        Parameters
        ----------
        n_setup_in : str
            The name of the input configuration resource
        n_template_out : str
            The name of the output template resource collection
        fov : float
            The field of view for which to generate the templates in radians
        """
        super().__init__()
        self.n_config_in = n_setup_in
        self.n_template_out = n_template_out
        self.fov = fov

    def apply(self, resources: list[BaseResource]) -> TemplateResource:
        """Generate templates for a planet at each point in the grid.

        Parameters
        ----------
        resources : list[BaseResource]
            List of resources to be used in the module.

        Returns
        -------
        TemplateResource
            The generated template resource.
        """
        print('Generating templates...')

        r_config_in = self.get_resource_from_name(self.n_config_in)
        time = r_config_in.phringe.get_time_steps()
        wavelength = r_config_in.phringe.get_wavelength_bin_centers()

        diff_ir = r_config_in.phringe.get_diff_instrument_response_theoretical(
            time, wavelength, self.fov, r_config_in.phringe.get_nulling_baseline()
        )

        template_diff_counts = (
                diff_ir
                * r_config_in.observation.detector_integration_time
                * r_config_in.phringe.get_wavelength_bin_widths()[None, :, None, None, None]
        )

        r_template_out = TemplateResource(
            name=self.n_template_out,
            grid_coordinates=get_meshgrid(self.fov, self.grid_size, self.device),
        )
        r_template_out.set_data(template_diff_counts)

        print('Done')
        return r_template_out
