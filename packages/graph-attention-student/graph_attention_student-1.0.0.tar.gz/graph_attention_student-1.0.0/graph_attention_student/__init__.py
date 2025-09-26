__author__ = """Jonas Teufel"""
__email__ = "jonseb1998@gmail.com"
__version__ = "0.1.0"

# Megan Model
from graph_attention_student.torch.megan import Megan, MeganEnsemble
from graph_attention_student.torch.data import SmilesDataset
from graph_attention_student.torch.data import data_from_graph
from graph_attention_student.torch.data import data_list_from_graphs

# Utils
from graph_attention_student.utils import PATH
from graph_attention_student.utils import get_version
