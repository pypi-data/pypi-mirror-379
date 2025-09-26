#!/usr/bin/env python
import asyncio
import os
import shutil

from tests.util import protoc

# Force pure-python implementation instead of C++, otherwise imports
# break things because we can't properly reset the symbol database.
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"


async def generate_test(
    name,
    semaphore: asyncio.Semaphore,
    *,
    reference: bool = False,
    pydantic: bool = False,
    descriptors: bool = False,
    client_generation: str = "async_sync",
):
    await semaphore.acquire()

    dir_path = os.path.dirname(os.path.realpath(__file__))

    options = []
    if reference:
        options.append("reference")
    if pydantic:
        options.append("pydantic")
    if descriptors:
        options.append("descriptors")

    input_dir = dir_path + "/inputs/" + name
    output_dir = dir_path + "/outputs/" + name + ("_" + "_".join(options) if options else "")

    os.mkdir(output_dir)

    stdout, stderr, returncode = await protoc(
        input_dir,
        output_dir,
        reference=reference,
        pydantic_dataclasses=pydantic,
        google_protobuf_descriptors=descriptors,
        client_generation=client_generation,
    )

    if options:
        options_str = ", ".join(options)
        options_str = f" ({options_str})"
    else:
        options_str = ""

    if returncode == 0:
        print(f"\033[31;1;4mGenerated output for {name!r}{options_str}\033[0m")
    else:
        print(f"\033[31;1;4mFailed to generate reference output for {name!r}{options_str}\033[0m")
        print(stderr.decode())

    semaphore.release()


async def main_async():
    # Don't compile too many tests in parallel
    semaphore = asyncio.Semaphore(os.cpu_count() or 1)

    tasks = [
        generate_test("any", semaphore),
        generate_test("bool", semaphore, pydantic=True),
        generate_test("bool", semaphore, reference=True),
        generate_test("bool", semaphore),
        generate_test("bytes", semaphore, reference=True),
        generate_test("bytes", semaphore),
        generate_test("casing_inner_class", semaphore),
        generate_test("casing", semaphore, reference=True),
        generate_test("casing", semaphore),
        generate_test("compiler_lib", semaphore),
        generate_test("deprecated", semaphore, reference=True),
        generate_test("deprecated", semaphore, client_generation="async"),
        generate_test("documentation", semaphore, client_generation="async"),
        generate_test("double", semaphore, reference=True),
        generate_test("double", semaphore),
        generate_test("encoding_decoding", semaphore),
        generate_test("enum", semaphore, reference=True),
        generate_test("enum", semaphore),
        generate_test("example_service", semaphore, client_generation="async"),
        generate_test("features", semaphore),
        generate_test("field_name_identical_to_type", semaphore, reference=True),
        generate_test("field_name_identical_to_type", semaphore),
        generate_test("fixed", semaphore, reference=True),
        generate_test("fixed", semaphore),
        generate_test("float", semaphore, reference=True),
        generate_test("float", semaphore),
        generate_test("google_impl_behavior_equivalence", semaphore, reference=True),
        generate_test("google_impl_behavior_equivalence", semaphore),
        generate_test("google", semaphore),
        generate_test("googletypes_request", semaphore, client_generation="async"),
        generate_test("googletypes_response_embedded", semaphore, client_generation="async"),
        generate_test("googletypes_response", semaphore, client_generation="async"),
        generate_test("googletypes_struct", semaphore, reference=True),
        generate_test("googletypes_struct", semaphore),
        generate_test("googletypes_value", semaphore, reference=True),
        generate_test("googletypes_value", semaphore),
        generate_test("googletypes", semaphore, reference=True),
        generate_test("googletypes", semaphore),
        generate_test("grpclib_reflection", semaphore, descriptors=True, client_generation="async"),
        generate_test("grpclib_reflection", semaphore, client_generation="async"),
        generate_test("import_cousin_package_same_name", semaphore, descriptors=True),
        generate_test("import_cousin_package_same_name", semaphore),
        generate_test("import_service_input_message", semaphore, client_generation="async"),
        generate_test("int32", semaphore, reference=True),
        generate_test("int32", semaphore),
        generate_test("invalid_field", semaphore, pydantic=True),
        generate_test("invalid_field", semaphore),
        generate_test("manual_validation", semaphore, pydantic=True),
        generate_test("manual_validation", semaphore),
        generate_test("map", semaphore, reference=True),
        generate_test("map", semaphore),
        generate_test("mapmessage", semaphore, reference=True),
        generate_test("mapmessage", semaphore),
        generate_test("message_wrapping", semaphore),
        generate_test("namespace_builtin_types", semaphore, reference=True),
        generate_test("namespace_builtin_types", semaphore),
        generate_test("namespace_keywords", semaphore, reference=True),
        generate_test("namespace_keywords", semaphore),
        generate_test("nested", semaphore, reference=True),
        generate_test("nested", semaphore),
        generate_test("nestedtwice", semaphore, reference=True),
        generate_test("nestedtwice", semaphore),
        generate_test("oneof_default_value_serialization", semaphore),
        generate_test("oneof_empty", semaphore, reference=True),
        generate_test("oneof_empty", semaphore),
        generate_test("oneof_enum", semaphore, reference=True),
        generate_test("oneof_enum", semaphore),
        generate_test("oneof", semaphore, pydantic=True),
        generate_test("oneof", semaphore, reference=True),
        generate_test("oneof", semaphore),
        generate_test("pickling", semaphore),
        generate_test("proto3_field_presence_oneof", semaphore, reference=True),
        generate_test("proto3_field_presence_oneof", semaphore),
        generate_test("proto3_field_presence", semaphore, reference=True),
        generate_test("proto3_field_presence", semaphore),
        generate_test("recursivemessage", semaphore, reference=True),
        generate_test("recursivemessage", semaphore),
        generate_test("ref", semaphore, reference=True),
        generate_test("ref", semaphore),
        generate_test("regression_387", semaphore),
        generate_test("regression_414", semaphore),
        generate_test("repeated_duration_timestamp", semaphore, reference=True),
        generate_test("repeated_duration_timestamp", semaphore),
        generate_test("repeated", semaphore, reference=True),
        generate_test("repeated", semaphore),
        generate_test("repeatedmessage", semaphore, reference=True),
        generate_test("repeatedmessage", semaphore),
        generate_test("repeatedpacked", semaphore, reference=True),
        generate_test("repeatedpacked", semaphore),
        generate_test("rpc_empty_input_message", semaphore, client_generation="async"),
        generate_test("service_uppercase", semaphore, client_generation="async"),
        generate_test("service", semaphore),
        generate_test("signed", semaphore, reference=True),
        generate_test("signed", semaphore),
        generate_test("simple_service", semaphore),
        generate_test("stream_stream", semaphore),
        generate_test("timestamp_dict_encode", semaphore, reference=True),
        generate_test("timestamp_dict_encode", semaphore),
        generate_test("unwrap", semaphore),
        generate_test("validation", semaphore, pydantic=True),
    ]
    await asyncio.gather(*tasks)


def main():
    # Clean the output directory
    dir_path = os.path.dirname(os.path.realpath(__file__))

    shutil.rmtree(dir_path + "/outputs", ignore_errors=True)
    os.mkdir(dir_path + "/outputs")

    asyncio.run(main_async())


if __name__ == "__main__":
    main()
