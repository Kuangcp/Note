## 1、安装并启动

-   进官网下载ZooKeeper，地址为`https://www.apache.org/dyn/closer.cgi/zookeeper/`

-   将下载好的压缩包，解压缩，并进入ZooKeeper的文件夹

-   查看目录`conf`下是否含有`zoo.cfg`配置文件(因我下载的版本是3.4.12,发现conf下有文件`zoo_sample.cfg`,将文件`zoo_sample.cfg`在原有目录下复制并改名为`zoo.cfg`，因ZooKeeper的启动脚本默认是使用配置`conf/zoo.cfg`，若没有该配置，则会报错)

-   启动服务器命令为`bin/zkServer.sh start`

-   启动CLI的命令为`bin/zkCli.sh`

-   停止ZooKeeper服务的命令为`bin/zkServer.sh stop`

## 2、使用

-   创建Znodes：`create [参数] /path 数据`，例如：`create /FirstZnode "first ZooKeeper-app"`，起命令参数如下

    -   `-s`： 创建连续的Znode
    -   `-e`: 创建一个零时的Znode

-   获取Znodes: `get /path`,`/path`要与创建时的一直

-   监视znode的数据变化：`get /path [watch] 1`, 例如：`get /FirstZnode 1`，当`/FirstZnode`的数据发生变化时，将输出变化

-   设置znode的数据：`set /path data`，例如：`set /FirstNode "Hello"`

-   创建子Znode的方法与创建Znode的方法一样，但需要在路径中包含父路径：`create /parent/path data`,例如：`create /FirstNode/TestNode "test"`

-   显示子Znode：`ls /parent`,例如列出上一步创建的Znode`ls /FirstNode`

-   检查状态：`stat /path`,例如：`stat /FirstNode`

-   删除Znode:`rmr /path`,仅适用于无子Znode

## 3、[Java API](https://github.com/dragonhht/ZooKeeper-study/blob/master/src/test/java/hht/dragon/TestZooKeeper.java)

-   获取ZooKeeper连接

    ```
    ZooKeeper zooKeeper = new ZooKeeper(host, 5000, new Watcher() {
                public void process(WatchedEvent watchedEvent) {
                    if (watchedEvent.getState() == Event.KeeperState.SyncConnected) {
                        latch.countDown();
                    }
                }
            });
    ```

    -   参数说明 : `ZooKeeper(String connectionString, int sessionTimeout, Watcher watcher)`

    > `connectionString` : ZooKeeper集合主机。  
    > `sessionTimeout` : 以毫秒为单位会话超时。  
    > `watcher` : 一个执行对象“观察者”的接口。ZooKeeper 集合返回通过监控器对象的连接状态。


-   创建Znode : `create(String path, byte[] data, List<ACL> acl, CreateMode createMode)`

    ```
        public void createZnode() throws IOException, InterruptedException, KeeperException {
        ZooKeeper zoo = connect("localhost");
        byte[] data = "Java API Test".getBytes();
        // 调用create方法创建Znode
        zoo.create(ZNODE_PATH, data, ZooDefs.Ids.OPEN_ACL_UNSAFE,
                CreateMode.PERSISTENT);
        close(zoo);
    }
    ```

    -   参数说明： 

    > `path` : Znode的路径。例如 /myapp1, /myapp2, /myapp1/mydata1, myapp2/mydata1/myanothersubdata  
    > `data` : 在一个指定的znode路径存储数据  
    > `acl` : 要创建节点的访问控制列表。 ZooKeeperAPI提供了一个静态接口ZooDefs.Ids得到一些基本的ACL列表。例如，ZooDefs.Ids.OPEN_ACL_UNSAFE返回ACL开放的 znodes 列表。  
    > `createMode` : 节点的类型，可以是短暂的，连续的，或两者。这是一个枚举类型。

-   检查Znode是否存在：`exists(String path, boolean watcher)`

    -   参数说明

    > `path` : Znode 路径  
    > `watcher` : 布尔值，指定是否监视指定的znode与否


-   获取数据：`getData(String path, Watcher watcher, Stat stat)`

    ```
        public void getData() throws IOException, InterruptedException, KeeperException {
            ZooKeeper zoo = connect("localhost");
            byte[] data = zoo.getData(ZNODE_PATH, new Watcher() {
                @Override
                public void process(WatchedEvent watchedEvent) {
                    if (watchedEvent.getType() == Event.EventType.None) {
                        switch (watchedEvent.getState()) {
                            case Expired:
                                latch.countDown();
                                break;
                        }
                    } else {
                        String path = "/MyFirstZnode";
                        try {
                            byte[] bn = zoo.getData(path,
                                    false, null);
                            String data = new String(bn,
                                    "UTF-8");
                            System.out.println(data);
                            latch.countDown();

                        } catch(Exception ex) {
                            System.out.println(ex.getMessage());
                        }
                    }
                }
            }, null);
            System.out.println(new String(data, "UTF-8"));
            close(zoo);
        }
    ```

    -   参数说明

    > `path` : Znode 路径.  
    > `watcher` : Watcher类型的回调函数。ZooKeeper集合将通知通过观察者回调时指定的节点改变的数据。这是一次性的通知。  
    > `stat` : 返回 znode 元数据。

-   修改数据： `setData(String path, byte[] data, int version)`

    ```
    public void setData() throws IOException, InterruptedException, KeeperException {
            ZooKeeper zoo = connect("localhost");
            byte[] data = "修改数据".getBytes();
            zoo.setData(ZNODE_PATH, data, zoo.exists(ZNODE_PATH, true).getVersion());
            close(zoo);
        }
    ```

    -   参数说明

    > `path` : Znode 路径  
    > `data` : 数据存储在一个指定的znode路径。
    > `version` : 当前znode的版本。ZooKeeper更新数据在znode的版本号改变了以后。

-   获取子节点： `getChildren(String path, Watcher watcher)`

    ```
        public void getChild() throws IOException, InterruptedException, KeeperException {
            ZooKeeper zoo = connect("localhost");
            List<String> children = zoo.getChildren("/FirstNode", false);
            children.forEach(System.out::println);
            close(zoo);
        }
    ```

    -   参数说明

    > `path` : Znode 路径.  
    > `watcher` : 调用“Watcher”类型函数. ZooKeeper集合将通知在指定的 znode 被删除或znode以下子节点创建/删除。 这是一次性的通知。

-   删除Znode节点

    ```
        public void del() throws IOException, InterruptedException, KeeperException {
            ZooKeeper zoo = connect("localhost");
            zoo.delete(ZNODE_PATH, zoo.exists(ZNODE_PATH, true).getVersion());
            close(zoo);
        }
    ```

    -   参数说明

    > `path` : Znode 路径   
    > `version` : 当前 znode 的版本
