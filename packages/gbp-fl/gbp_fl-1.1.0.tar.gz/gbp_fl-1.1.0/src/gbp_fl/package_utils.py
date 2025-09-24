"""Utilities for working with Packages"""

import datetime as dt
from concurrent.futures import ThreadPoolExecutor, wait
from functools import partial
from pathlib import PurePath as Path

from gbp_fl.gateway import gateway
from gbp_fl.records import Repo
from gbp_fl.types import BinPkg, Build, ContentFile, ContentFileInfo, Package


def index_build(build: Build, repo: Repo) -> None:
    """Save the given Build's packages to the database"""
    executor = ThreadPoolExecutor()

    try:
        packages = gateway.get_packages(build) or []
    except LookupError:
        return

    wait(executor.submit(index_package, package, build, repo) for package in packages)


def index_package(package: Package, build: Build, repo: Repo) -> None:
    """Save the files from the given build/package"""
    items = gateway.get_package_contents(build, package)
    content_file = partial(make_content_file, build, package)

    repo.files.bulk_save(
        content_file(ContentFileInfo(name=i.name, mtime=int(i.mtime), size=i.size))
        for i in items
        if not i.isdir() and i.name.startswith(("image/", "./"))
    )


def make_content_file(
    build: Build, gbp_package: Package, metadata: ContentFileInfo
) -> ContentFile:
    """Return a ContentFile given the parameters"""
    path = metadata.name.removeprefix("image").removeprefix(".")

    return ContentFile(
        path=Path(path),
        binpkg=make_binpkg(build, gbp_package),
        size=metadata.size,
        timestamp=dt.datetime.fromtimestamp(metadata.mtime, tz=dt.UTC),
    )


def make_binpkg(build: Build, gbp_package: Package) -> BinPkg:
    """Create a BinPkg given the build and Package"""
    return BinPkg(
        build=Build(machine=build.machine, build_id=build.build_id),
        cpvb=f"{gbp_package.cpv}-{gbp_package.build_id}",
        repo=gbp_package.repo,
        build_time=dt.datetime.fromtimestamp(gbp_package.build_time, dt.UTC),
    )
