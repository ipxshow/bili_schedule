# bili_schedule
定时启动运行于linux上的BiliHelper服务的python脚本

## 环境要求
linux

python3
### python包
包名|
--|
requests|
os|
schedule|

## 配置项
参数|说明|举例
--|--|--|
password|启动服务时需要的密码|略
sckey|server酱微信推送的sckey自行获取，不填写不推送到微信,[地址](http://sc.ftqq.com/3.versio)|略
start_time|服务启动的时间|注意是`00:00`格式，不满10位0补齐，如：02:30
stop_time|服务停止的时间|注意项同上

## 运行脚本
`nohup python bili_schedule.py &`

## 查看脚本是否运行
`ps -ef | grep python`
