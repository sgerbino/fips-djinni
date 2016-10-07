import os
import yaml
from subprocess import call
import genutil as util

djinni = os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(__file__)), '..', 'djinni', 'src', 'run'))

default_args = yaml.load("{"
                         "java-out: java,"
                         "cpp-out: src/interface,"
                         "objc-out:  objc,"
                         "objcpp-out: objc,"
                         "jni-out: jni,"
                         "objcpp-include-cpp-prefix: interface/,"
                         "cpp-optional-header: \"<experimental/optional>\","
                         "cpp-optional-template: \"std::experimental::optional\","
                         "cpp-namespace: mobilepp,"
                         "java-package: io.github.mobilepp,"
                         "jni-namespace: mobilepp_jni,"
                         "objc-type-prefix: MPP,"
                         "objcpp-namespace: mobilecpp_obj,"
                         "ident-cpp-enum: foo_bar,"
                         "ident-cpp-field: foo_bar,"
                         "ident-cpp-method: foo_bar,"
                         "ident-cpp-enum-type: foo_bar,"
                         "ident-cpp-type-param: foo_bar,"
                         "ident-cpp-local: foo_bar,"
                         "ident-cpp-file: foo_bar,"
                         "ident-cpp-type: foo_bar,"
                         "ident-java-field: mFooBar,"
                         "ident-jni-class: NativeFooBar,"
                         "ident-jni-file: native_foo_bar"
                         "}")

def generate(input, out_src, out_hdr, args = default_args):
                if util.isDirty(None, [input], []):
                                cmd = []
                                cmd.append(djinni)
                                cmd.append('--idl')
                                cmd.append(input)
                                for key, value in args.items():
                                                cmd.append('--{}'.format(key))
                                                cmd.append(value)
                                call(cmd)
