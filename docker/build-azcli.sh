#!/bin/bash
tmp_dir='tmp/azcli/'

if [ "$1" ];then
    tag="$1"
    build_tag="gdapenny/study/azcli:$tag"
    git clone -b $tag --single-branch https://github.com/lorraineliu/azcli.git $tmp_dir
    pushd $tmp_dir
    /bin/rm -rf .git
    popd

    sed -e "s/^ENV TAG.*$/ENV TAG $tag/" Dockerfile.azcli >Dockerfile.azcli.tmp
    /bin/mv Dockerfile.azcli.tmp Dockerfile.azcli

    docker build -t $build_tag -f Dockerfile.azcli .
    rm -rf $tmp_dir
fi
