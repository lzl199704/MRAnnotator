import nibabel as nib
import numpy as np


def get_orientation(nifti_file):
    ### This function will check and print the orientation of the image data
    # Load the NIfTI file
    img = nib.load(nifti_file)
    
    # Get the affine matrix
    affine = img.affine
    
    # Define the standard coordinate system axes
    axis_codes = nib.aff2axcodes(affine)
    
    # Return the orientation as a string
    orientation = ''.join(axis_codes)
    print("Orientation of the NIfTI file is:", orientation)
    return orientation


def convert_RAS_to_LAS(nifti_file_path):
    ### This function will convert RAS nifti file to LAS nifti file
    
    # Load the original NIfTI file
    img = nib.load(nifti_file_path)
    
    # Get the image data array
    data = img.get_fdata()
    data = np.uint8(data)
    
    # Flip the data along the x-axis to change R to L
    flipped_data = np.flip(data, axis=0)  # axis 0 is the x-axis in RAS
    
    # Update the header to reflect the new orientation
    # This involves flipping the x-axis sign in the affine matrix
    new_affine = img.affine.copy()
    new_affine[0, 0] *= -1  # Change the sign of the x-component

    # Create a new NIfTI image with the flipped data and updated affine
    new_img = nib.Nifti1Image(flipped_data, affine=new_affine, header=img.header)
    
    # Save the new image back to the original file path
    nib.save(new_img, nifti_file_path)
    print(f"Converted and overwritten the NIfTI file at {nifti_file_path}")
    
if __name__ == "__main__":
    nifti_path = 'sample.nii.gz'
    
    orientation = get_orientation(nifti_file_path)
    convert_RAS_to_LAS(nifti_file_path)
    