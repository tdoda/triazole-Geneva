# -*- coding: utf-8 -*-
import numpy as np
import netCDF4 as nc
import xarray as xr

    
#%%############################################################################
def export_netCDF(filename,general_attributes,dimensions,variables,data):
    """Function export_netCDF

    Export data to a netCDF file

    Inputs:
    ----------
    filename (string): netCDF filename with path included
    general_attributes (dictionary): file attributes with the format {"name_attribute1": "attribute1_value",…}
    dimensions (dictionary): dimensions with the format {'name_dimension1': {'dim_name': 'name_dimension1', 'dim_size': ...},…}
    variables (dictionary): variable names with the format {'name_variable1': {'var_name': 'name_variable1', 'dim': ('name_dim1',’name_dim2’,…),'unit': “name_units”, 'longname': 'long_name_variable1', 'var_type':'float' or 'str'},…}
    data (dictionary): data to export with the format {“name_variable1”:numpy_array,…}
    vartype 
    
        
    Outputs: None
    
    """
    with nc.Dataset(filename, mode='w', format='NETCDF4') as nc_file:
        for key in general_attributes:
            setattr(nc_file, key, general_attributes[key])
            
        for key, values in dimensions.items():
             nc_file.createDimension(values['dim_name'], values['dim_size'])
    
    
        for key, values in variables.items(): 
            if 'var_type' not in values.keys() or values["var_type"]=="float":
                var = nc_file.createVariable(values["var_name"], np.float64, values["dim"], fill_value=np.nan)
            elif values["var_type"]=="str":
                var = nc_file.createVariable(values["var_name"], str, values["dim"])
            else:
                raise Exception("Variable type is unknown")
            
            if "unit" in values:
                var.units = values["unit"]
            else: 
                var.units = values["units"]
                
            if "longname" in values:
                var.long_name = values["longname"]
            else:  
                var.long_name = values["long_name"]
                
            if key in data.keys():
                if 'var_type' not in values.keys() or values["var_type"]=="float":
                    var[:] = data[key]
                else:
                    for k in range(len(data[key])):
                        var[k]=data[key][k]
            else:
                raise Exception("Data is missing for {}".format(key))

    print("Data exported to netCDF!")

#%%############################################################################   
def read_netCDF(pathname):
    """Function read_netCDF

    Read a netCDF file with the netCDF4 package and convert it to a dictionary.

    Inputs:
    ----------
    pathname (string): netCDF filename with path included
    
        
    Outputs:
    ----------
    nc_data (dictionary): dataset as a dictionary of numpy arrays
    nc_genatt (dictionary): general attributes
    nc_varatt (dictionary): variable attributes
    nc_dim (dictionary): variable dimensions
    """
    
    with nc.Dataset(pathname, 'r') as nc_obj:
        nc_data, nc_genatt, nc_varatt, nc_dim=netCDF2dict(nc_obj)

    
    return nc_data, nc_genatt, nc_varatt, nc_dim

#%%############################################################################
def netCDF2dict(nc):
    """Function netCDF2dict

    Converts a netCDF object to a dictionary
    
    """
    nc_data=dict()
    nc_genatt=dict()
    nc_varatt=dict()
    nc_dim=dict()

    for key,value in nc.variables.items():
        if value.dtype==np.float64:
            nc_data[key]=value[:].data
        else:
            nc_data[key]=value[:]
        nc_varatt[key]=dict()
        nc_varatt[key]["var_name"]=key
        for att in value.ncattrs():     
            nc_varatt[key][att]=getattr(value,att)
        nc_varatt[key]["dim"]=value.dimensions
            
    for dim_name in nc.dimensions.keys():
        nc_dim[dim_name]={"dim_name":nc.dimensions[dim_name].name,"dim_size":nc.dimensions[dim_name].size}
            

    for att in nc.ncattrs():
        nc_genatt[att]=getattr(nc,att)

                
    return nc_data, nc_genatt, nc_varatt, nc_dim

#%%############################################################################
def ncdicts_to_xarray(nc_data, nc_genatt, nc_varatt, nc_dim):
    """
    Convert netCDF dictionaries (from netCDF2dict) to an xarray.Dataset
    equivalent to xr.open_dataset()
    """

    data_vars = {}
    coords = {}

    # Loop over all variables
    for var_name, data in nc_data.items():
        var_info = nc_varatt[var_name]
        dims = var_info["dim"]

        # Variable attributes (exclude internal keys)
        attrs = {
            k: v for k, v in var_info.items()
            if k not in ["var_name", "dim"]
        }

        # Coordinate variable if its name matches a dimension
        if len(dims) == 1 and dims[0] == var_name:
            coords[var_name] = (dims, data, attrs)
        else:
            data_vars[var_name] = (dims, data, attrs)

    # Create dataset
    ds = xr.Dataset(
        data_vars=data_vars,
        coords=coords,
        attrs=nc_genatt
    )

    return ds
#%%############################################################################
def read_netCDF_xr(pathname):
    """Function read_netCDF_xr

    Read a netCDF file as an xarray by converting it to dictionaries first, working for relative or absolute paths without non-ASCII characters 

    Inputs:
    ----------
    pathname (string): netCDF filename with path included
        
    Outputs:
    ----------
    data_xr (xarray dataset): netCDF data as an xarray
    
    """
    
    nc_data, nc_genatt, nc_varatt, nc_dim = read_netCDF(pathname)

    data_xr = ncdicts_to_xarray(nc_data, nc_genatt, nc_varatt, nc_dim)
    
    return data_xr

#%%############################################################################
def export_netcdf_xr(filename, ds):
    """
    Export an xarray.Dataset using export_netCDF().
    """

    # Global attributes
    general_attributes = dict(ds.attrs)

    # Dimensions
    dimensions = {
        dim: {
            "dim_name": dim,
            "dim_size": ds.sizes[dim]
        }
        for dim in ds.dims
    }

    # Variables
    variables = {}
    data = {}

    for name, da in ds.variables.items():

        # Determine variable type
        if da.dtype.kind in ("U", "S", "O"):
            var_type = "str"
        else:
            var_type = "float"

        variables[name] = {
            "var_name": name,
            "dim": da.dims,
            "var_type": var_type,
            "units": da.attrs.get("units", ""),
            "long_name": da.attrs.get("long_name", ""),
        }

        data[name] = da.values

    export_netCDF(
        filename=filename,
        general_attributes=general_attributes,
        dimensions=dimensions,
        variables=variables,
        data=data,
    )
