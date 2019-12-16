
# Recipes

## Recipe Ingredients

Each recipe is built from two ingredients:

1. The interface specification file.
2. The template specification file.

The **interface** will specify the value of the parameters that get substituted into the **template**.

The **template** contains the commands that need to be executed. The **template** will have
placeholders for the parameter values that the user will need to enter in the interface.

The interface + template will generate a script that the site can execute.

The software will generate an web interface for each parameter specified in the interface. It is this interface where users are able to select the values that their recipe needs to operate.


A recipe consists of a "JSON definition file" and a "script template".

The simplest JSON definition file is

    {}

A simple script template might contain just:

    echo 'Hello World!'


The **Results** are created by applying a **Recipe** on **Data**.

## Create a Recipe 

Creating a recipe can be done using the command line or web interface.

Command line options:
- Directly upload json and script template to a given recipe.

Web interface options:

- **Clone a recipe** - Remains synchronized with original recipe. Changes are carried over from the original.

- **Copy a recipe** - Create a new of a recipe that is a direct copy of another.


### Using the Command Line

Use the `recipe` management command to directly add to a project.

    $ python manage.py recipe --help
    
    usage: manage.py recipe [-h] --pid PID --rid RID [--json JSON]
                        [--template TEMPLATE] [--info INFO] [--name NAME]
                        [--image IMAGE] [--update] [--version] [-v {0,1,2,3}]
                        [--settings SETTINGS] [--pythonpath PYTHONPATH]
                        [--traceback] [--no-color] [--force-color]

    Adds recipe to a project

    optional arguments:
      -h, --help            show this help message and exit
      --pid PID             Project id.
      --rid RID             Recipe id.
      --json JSON           Recipe json path.
      --template TEMPLATE   Recipe template path (optional)
      --info INFO           Recipe description (optional)
      --name NAME           Recipe name
      --image IMAGE         Recipe image path
      --update              Updates the recipe


For example, the command below would add a recipe named `New recipe` to project with uid `project 1`.

    python manage.py recipe --pid project 1 --name New recipe --json < interface file > --template < script template > 


### Using Web Interface

Open on a recipe of interest and click on the `Copy` button on the menu bar.
![](images/copy-clone.png)

After clicking `Copy` the recipe is in your clipboard. Open the `Recipe` tab of any project to view your clipboard.

Once your clipboard has recipes, you can  **clone** or **copy**.
 

Cloning allows your recipes to stay up to date with an original source. 

**Note** You can clone with `Read Access` and edit the cloned recipe with `Write Access` to the original.

To clone the recipes in your clipboard, click the `Paste as clone` at the top of the `Recipes` tab.

![](images/paste-as-clone.png)


Copying creates recipes with the same specifications as the ones in the clipboard.

To copy the recipes , click the `Paste as new` at the top of the `Recipes` tab.
![](images/paste-as-new.png)


## Interface Specification 

The JSON definition file lists the parameters and allows the interface to be rendered.
Here is an example JSON definition file:

```
{
  foo: {
    label: Enter the name
    help: The name to appear after the greeting
    display: TEXTBOX
    value: World!
  }
}
```

the parameter name is `foo`, the default value is `World!`. The `display` field specifies the type of the HTML widget, the `label` and  `help` fields describe the interface. The interface generated from this specification file looks like this:

![](images/interface-1.png)


## Interface Builder
One of the useful features in our web interface is the `Interface Builder.` 

![](images/builder.png)

Every interface option is in this dropdown and 


## Code Builder




## Data Field

A "data" unit in the `recipes` app is a directory that may contain one or more (any number of files).

### Data value

Each recipe parameter will have an automatic attribute called `value` that contains either the selected value (if  the parameter is user supplied) or the first file from the `table-of-contents`. For data consisting of a single file one may use the value directly.

    fastqc {{reads.value}}

### Table of Contents

Each recipe parameter will have an automatically generated attribute called `toc` (table of contents) that returns the list of the file paths in the data.

The file paths are absolute paths. The `toc` can be used to automate the processing of data. For example
a data directory named `reads` contains several FASTQ files with `.fq` extensions. To run `fastqc` on each file that matches that
the recipe may use:

    cat {{reads.toc}} | grep .fq | parallel fastqc {}

### Data Source

When a recipe parameter indicates the source of the parameter as `PROJECT` it will be populated from the data in the project that matches the type.

    reference: {
        label: Reference Genome
        display: DROPDOWN
        type: FASTA
        source: PROJECT
    }

Only data that matches the tage `FASTA` will be shown in the dropdown menu.

### Data Types

Data types are labels (tags) attached to each data that help filtering them in dropdown menus. More than one data type may be listed as comma separated values.
The data types may be any word (though using well recognized names: BED, GFF is recommended).

Data that exists on a filesystem may be linked into the Biostar Engine from the command line. 
This means that no copying/moving of data is required. 
The only limitation is that of the filesystem.


## Recipe Template

A recipe is a script that has template markers for filling in parameters. In the case for the `foo` variable above, we can access its value via:

    echo 'Hello {{foo.value}}'

Recipes are using [Django templates][templates] and may contain Django template specific constructs.

When the recipe is run the template will be substituted according to the interface value entered by the user. If the default value is kept it will produce the script:

    echo 'Hello World!'

## Recipe Execution

Before executing the recipe the script template is rendered with the JSON data and is filled into the template.

    template + JSON -> script

The script is then executed at the command line.

The recipe execution creates a `Result` objects.


# Results

Result directories consists of all files and all the metadata created by the recipe as it is executed on the input data.  
Each run of a recipe will generate a *new* result directory. 
Users may inspect, investigate and download any of the files generated during the recipe run. 
Additionally, users may copy a result file as new data input for another recipe. 


[templates]: https://docs.djangoproject.com/en/2.2/topics/templates/

## Output Directory

Once the recipe runs a results directory is created that contains the following:

- the code for the recipe
- the standard out and error stream content
- all files created by the recipe

The results directory is a snapshot of all files generated when the recipe has been run, including the recipe itself.


## Job Runner
