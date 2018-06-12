# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class SHAREHOLDER_FLOATING_TOP10(Base):

    __tablename__ = 'SHAREHOLDER_FLOATING_TOP10'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, nullable=False, comment="公司ID")
    company_name = Column(String(100), nullable=False, comment="公司名称")
    stock_code = Column(String(12), nullable=False, comment="股票代码")
    end_date = Column(Date, nullable=False, comment="截止日期")
    pub_date = Column(Date, nullable=False, comment="公告日期")
    change_reason_id = Column(Integer, comment="变动原因编码")
    change_reason = Column(String(120), comment="变动原因")
    shareholder_rank = Column(Integer, nullable=False, comment="股东名次")
    shareholder_id = Column(Integer, comment="股东ID")
    shareholder_name = Column(String(200), comment="股东名称")
    shareholder_name_en = Column(String(150), comment="股东名称(英文)")
    shareholder_class_id = Column(Integer, comment="股东编码类别")
    shareholder_class = Column(String(150), comment="股东类别")
    share_number = Column(DECIMAL(20, 4), comment="持股数量(股)")
    share_ratio = Column(DECIMAL(10, 4), comment="持股比例(%)")
    sharesnature_id = Column(Integer, comment="股份性质编码")
    sharesnature = Column(String(120), comment="股份性质")
    # status = Column(TINYINT(display_width=4), default=0, comment="是否同步,0:未同步,1:已同步")
    # addTime = Column(TIMESTAMP, default=datetime.datetime.now, comment="插入时间")
    # modTime = Column(TIMESTAMP, default=datetime.datetime.now, comment="最后修改时间")
