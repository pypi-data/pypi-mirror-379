use std::env;
use std::path::PathBuf;

fn main() {
    //pyo3_build_config::add_extension_module_link_args();

    // for debug only
    // env::set_var("LIBRARY_PATH", "/home/erik.vonreis/fakeroot/lib");
    // env::set_var("LD_LIBRARY_PATH", "/home/erik.vonreis/fakeroot/lib");
    // let inc_dir = "/home/erik.vonreis/fakeroot/include";
    // env::set_var("C_INCLUDE_PATH", inc_dir);
    // env::set_var("CPLUS_INCLUDE_PATH", inc_dir);
    //
    // println!("cargo:rustc-link-search=/home/erik.vonreis/fakeroot/lib");
    // println!("cargo:rustc-link-search=/lib/gcc/x86_64-linux-gnu/12");

    // needed because for some unknown reason, rust can forget about some
    // default library directories in some cases.
    // println!("cargo:rustc-link-search=/usr/lib/x86_64-linux-gnu/");

    // println!("cargo:rustc-link-arg=-static-libstdc++");
    // println!("cargo:rustc-link-arg=-static-libgcc");
    //
    println!("cargo:rustc-link-lib=gds-sigp");
    println!("cargo:rustc-link-lib=fftw3");

    // #[cfg(any(feature = "python", feature="python-pipe"))]
    // {
    //     // link to python - this is cribbed from pyo3 code.
    //     // In other projects, pyo3 does this correctly
    //     // but for some reason dttlib needs to manually link to python.
    //     // Get Python configuration
    //     let python_config = pyo3_build_config::get();

    //     // Add Python library search path
    //     if let Some(d) = &python_config.lib_dir {
    //         println!("cargo:rustc-link-search={}", d);
    //     }

    //     println!("cargo:rustc-link-lib={}", &python_config.lib_name.as_ref().unwrap());
    // }

    let bindings = bindgen::Builder::default()
        .header("wrapper.h")
        .generate()
        .expect("Unable to generate bindings");

    let out_path = PathBuf::from(env::var("OUT_DIR").unwrap());
    bindings
        .write_to_file(out_path.join("bindings.rs"))
        .expect("Couldn't write bindings");
}
