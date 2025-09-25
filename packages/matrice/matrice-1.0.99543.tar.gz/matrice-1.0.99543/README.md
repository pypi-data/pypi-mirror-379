## Introduction

The matrice-datasets-sdk is a python package that has APIs defined in it to perform operations related to datasets on the matrice.ai platform.

### Installation (will update it after we release this repo as a python package):

```
git clone https://github.com/matrice-ai/matrice-dataset-sdk.git
cd matrice-database-sdk
```

## File structure
```
python_sdk/
├── docs/
│   ├── Be-Annotation.md
│   ├── Be-Dataset.md
│   ├── Be-Deployment.md
│   ├── Be-Model.md
│   ├── Be-Project.md
│   ├── Be-Resources.py
│   ├── Be-User.py
│   └── Inference-Optimization.md
├── src/
│   ├── annotation.py
│   ├── dataset.py
│   ├── deployment.py
│   ├── inference_optim.py
│   ├── models.py
│   ├── resources.py
│   ├── rpc.py
│   └── token_auth.py
├── test/
│   ├── annotation.ipynb
│   ├── config.py
│   ├── dataset.ipynb
│   ├── deployment.ipynb
│   ├── inference_optim.ipynb
│   ├── projects.ipynb
│   ├── models.ipynb
│   ├── resources.ipynb
│   └── user.ipynb
├── setup.py
└── README.md
```

### Usage:

#### Class dataset.Dataset [[Source]](https://github.com/matrice-ai/matrice-dataset-sdk/blob/main/src/dataset.py)

All the operations on a dataset will be performed via the methods of the `Dataset` class. So, before performing any operation on the datasets, we need to instantiate an object of the `Dataset` class.

```python
class dataset.Dataset(project_id, dataset_id=None, email="", password="")
```

This constructor should be used to instantiate an object of the `Dataset` class. 
Parameters in the constructor:

* `project_id`: string, the id of the project in which you want to create the dataset 
* `dataset_id`: string, the id of the dataset on which you want to perform operations 
* `email`:  string, email associated with the matrice.ai platform account
* `password`: string, password for your account corresponding to `email` for the matrice.ai platform

If you want to create a new dataset and perform some operations on it, you can instantiate an object of the `Dataset` class without setting the value of `dataset_id`. 

```python3

# import Dataset class 
from src.dataset import Dataset

# set the value of my_email to the email associated with the matrice.ai account
my_email = "example@gmail.com"

# set the value of my_password to the password corresponding to `my_email` for matrice.ai platform
my_password = "password"

# set the value of project_id to the id of the project in which you want to create the dataset 
project_id = "abcc123facc"

# instantiate an object of the Dataset class
d1 = Dataset(project_id = project_id,email=email, password=password)

```

If you want to perform any operation on an already created dataset, you will have to set the value of `dataset_id` to the id of the dataset on which you want to perform operations while instantiating the object of the `Datasets` class.

```python3

# set the value of my_email to the email associated with the matrice.ai account
my_email = "example@gmail.com"

# set the value of my_password to the password corresponding to `my_email` for matrice.ai platform
my_password = "password"

# set the value of project_id to the id of the project in which the dataset you want to access exists
project_id = "abcc123facc"

# set the value of dataset_id to the id of the dataset on which you want to perform operations 
dataset_id = "addfc123facc"

# instantiate an object of the Dataset class
d1 = Dataset(project_id = project_id, dataset_id = dataset_id ,email=email, password=password)

```

Note:
All the methods defined in `Dataset` will return `response`, `error`, and `message`. The `response` will be the response given by the `matrice.ai` backend, `error` will represent the error message(if there is any error else `None`) and `message` will be a simple text message that provides information about the status of the task being requested to execute.


#### Create a dataset:
To create a dataset in the matrice.ai platform using the `matrice-datasets-sdk`, we can use the `create_dataset()` method defined in the `dataset.Dataset` class. Before, calling the `create_dataset` method, we instantiate an object of the `Dataset` class.

```
dataset.Dataset.create_dataset(self, name, type, is_unlabeled, source, source_url, dataset_description="", version_description="")
```

Parameters in the method:

* `name`: string, name of the dataset to be created 
* `type`: string, type of the task of the dataset (for now we support `"classification"` and `"detection"` types)
* `is_unlabeled`:  boolean (True/False), True if the dataset is unlabeled
* `source`: string, Source for dataset files (currently supported only "url")
* `source_url` : string, URL of the dataset zipped file
* `dataset_description`: string, Optional field that is used to store some information about the dataset we are creating 
* `version_description`: string, Optional field that is used to store some information about the `v1.0` of the dataset


In the matrice.ai platform, we can create a new dataset either by uploading local `zip` files or by using a URL of the dataset files stored somewhere remotely.

To create a dataset using the URL of the dataset files, we pass source="url" and pass URL of files as the `source_url` argument.

```python3
resp, err, msg = d1.create_dataset(name = "dataset-name",type="detection", is_unlabeled=False, source="url", source_url="https://example.com/sample2_data.tar.gz", dataset_description="Dataset created using matricesdk", version_description="Initial Version")
```

#### Add new samples to the existing dataset:

To add new samples to the existing dataset, we can use the `add_new_samples()` method defined in the `dataset.Dataset` class.

```
dataset.Dataset.add_new_samples(self,old_version, new_version, is_unlabeled, source, source_url, dataset_description="", version_description="")
```

Parameters in the method:

* `old_version`: string, the version of the dataset to which you want to add samples 
* `new_version`: string, the new version of the dataset with added samples (set new_version equal to old_version argument if you don't want to create a new version)
* `is_unlabeled`:  boolean (True/False), True if the dataset is unlabeled
* `source`: string, Source for dataset files (currently supported only "url")
* `source_url`: string, URL of the dataset zipped file
* `dataset_description`: string, Optional field if set to a string updates existing description of the dataset 
* `version_description`: string, Optional field. Used to set the description of a version if we are creating a new version or used to update the description of a version if we are updating an existing version


In the matrice.ai platform, we can add new samples to the existing dataset either by uploading local `zip` files or by using a URL of the dataset files stored somewhere remotely.

To add new samples to the existing dataset using the URL of the dataset files, we pass source="url" and pass URL of files as the `source_url` argument.

```python3
resp, err, msg = d1.add_new_samples(old_version="v1.0", new_version="v1.0", is_unlabeled=False, source="url", source_url="https://myexample.com/sample2_data.tar.gz")
```

The python statement above will add new samples to version `v1.0` of the `d1` dataset using the files in the `source_url`. It will not create a new version in this case.

```python3
resp, err, msg = d1.add_new_samples(old_version="v1.0", new_version="v1.1", is_unlabeled=False, source="url", source_url="https://s3.us-west-2.amazonaws.com/temp.matrice/sample2_data.tar.gz",version_description="Adding samples")
```

The python statement above will add new samples to version `v1.0` of the `d1` dataset using the files in the `source_url and store the final result as version `v1.1`.

#### Create dataset splits:

To move samples from one split to another split or create new random splits in the existing dataset, one can use the `split_dataset()` method defined in the `dataset.Dataset` class.

```
dataset.Dataset.split_dataset(self,old_version, new_version, is_random_split, train_num=0, val_num=0, test_num=0, unassigned_num=0.dataset_description="", version_description="",)
```

Parameters in the method:

* `old_version`: string, the version of the dataset in which you want to move samples from one split to another split or create new random splits
* `new_version`: string, the new version of the dataset with added samples (set new_version equal to old_version argument if you don't want to create a new version)
* `is_random_split`:  boolean (True/False), set to True if you want to create fresh new random splits
* `train_num`: int, Number of samples you want to be in the training set
* `val_num`: int, Number of samples you want to be in the validation set
* `test_num`: int, Number of samples you want to be in the test set
* `unassigned_num`: int, Number of samples you want to be in the unassigned set
* `dataset_description`: string, Optional field if set to a string updates existing description of the dataset 
* `version_description`: string, Optional field. Used to set the description of a version if we are creating a new version or used to update the description of a version if we are updating an existing version

#### Delete a specific version of a dataset:

To delete a specific version of a dataset, we can use the `delete_version()` method defined in the `dataset.Dataset` class.

```
delete_version(self, version):
```

Parameters in the method:

* `version`: string, version of the dataset to be deleted

```python3
resp, err, msg = d1.delete_version("v1.2")
```

The Python statement above will delete version `v1.2` of the `d1` dataset.


#### Delete a dataset:

To delete a dataset, we can use the `delete_dataset()` method defined in the `dataset.Dataset` class.

```
delete_dataset(self)
```

```python3
resp, err, msg = d1.delete_dataset()
```

The Python statement above will delete the `d1` dataset.


#### Rename a dataset:

To rename a dataset, one can use the `rename_dataset()` method defined in the `dataset.Dataset` class.

```
rename_dataset(self, updated_name)
```

Parameters in the method:

* `updated_name`: string, the name you want the dataset to rename to

```python3
resp, err, message = d1.rename_dataset(updated_name="my_dataset")
```

The Python statement above will rename the `d1` dataset to `my_dataset`.


#### Get a list of all the datasets:

To get a list of all the datasets inside a project, one can use the `get_all_datasets()` method defined in the `dataset.Dataset` class.

```
get_all_datasets(self)
```

```python3
resp, err, message = d1.get_all_datasets()
```

The Python statement above will list all the datasets inside the `project_id` of `d1`.


#### Get information(details) about a dataset:

To get information about a particular dataset inside a project, we can use the `get_dataset_info()` method defined in the `dataset.Dataset` class.

```
get_dataset_info(self)
```

```python3
resp, err, message = d1.get_dataset_info()
```

The Python statement above will provide us with the information about `d1`.


#### Get a summary of a particular version of a dataset:

To get a summary of a particular version of a dataset, one can use the `get_version_summary()` method defined in the `dataset.Dataset` class.

```
get_version_summary(self, version)
```

Parameters in the method:

* `version`: string, version of the dataset whose summary you want to get

```python3
resp, err, msg = d1.get_version_summary("v1.0")
```

The Python statement above will provide us with the summary of version `v1.0` of dataset `d1`.


#### List all versions of a dataset:

To list all the versions of a dataset, one can use the `list_versions()` method defined in the `dataset.Dataset` class.

```
list_versions(self)
```

```python3
resp, err, msg = d1.list_versions()
```

The Python statement above will provide us with the latest version and the list of all versions of the dataset `d1`.


#### List all the label categories of a dataset:

To list all the label categories of a dataset, one can use the `list_categories()` method defined in the `dataset.Dataset` class.

```
list_categories(self)
```

```python3
resp, err, msg = d1.list_categories()
```

The Python statement above will provide us with all the label categories of the dataset `d1`.


#### List all the logs for a dataset:

To list all the logs for a dataset, one can use the `get_logs()` method defined in the `dataset.Dataset` class.

```
get_logs(self)
```

```python3
resp, err, msg = d1.get_logs()
```

The Python statement above will give us a list of all the logs for the dataset `d1`.


#### List all the dataset items in a dataset:

To list all the dataset items in a dataset, one can use the `list_all_dataset_items()` method defined in the `dataset.Dataset` class.

```
list_all_dataset_items(self, version)
```

Parameters in the method:

* `version`: string, version of the dataset whose items you want to get

```python3
resp, err, msg = d1.list_all_dataset_items(version="v1.0")
```

The Python statement above will give us a list of all the dataset items in version `v1.0` of the dataset `d1`.
