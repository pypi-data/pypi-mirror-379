import torch

from lifesimmc.core.modules.base_module import BaseModule
from lifesimmc.core.resources.base_resource import BaseResource
from lifesimmc.core.resources.image_resource import ImageResource


class CorrelationMapModule(BaseModule):
    """Module to calculate the correlation map of a template and data image.

    Parameters
    ----------
    n_data_in : str
        The name of the data input resource.
    n_template_in : str
        The name of the template input resource.
    n_image_out : str
        The name of the output image resource.
    """

    def __init__(
            self,
            n_data_in: str,
            n_template_in: str,
            n_image_out: str
    ):
        """Constructor method.

        Parameters
        ----------
        n_data_in : str
            The name of the data input resource.
        n_template_in : str
            The name of the template input resource.
        n_image_out : str
            The name of the output image resource.
        """
        self.n_data_in = n_data_in
        self.n_template_in = n_template_in
        self.n_image_out = n_image_out

    def apply(self, resources: list[BaseResource]) -> ImageResource:
        """Create a correlation map of the templates with the data.

        Parameters
        ----------
        resources : list[BaseResource]
            The resources to apply the module to.

        Returns
        -------
        ImageResource
            The resource containing the correlation map.
        """
        print('Calculating correlation map...')

        data_in = self.get_resource_from_name(self.n_data_in).get_data()
        template_counts_in = self.get_resource_from_name(self.n_template_in).get_data()

        y = data_in.flatten()
        x = template_counts_in.reshape(
            -1,
            template_counts_in.shape[-1],
            template_counts_in.shape[-1]
        )

        image = (
                torch.einsum('i,ijk->jk', y, x)
                # / torch.sqrt(torch.einsum('i, i->', y, y))
                / torch.sqrt(torch.einsum('ijk,ijk->', x, x))
        )

        r_image_out = ImageResource(self.n_image_out)
        r_image_out.set_image(image)

        print('Done')
        return r_image_out
