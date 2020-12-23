import React, { useEffect, useState } from 'react';
import axios from 'axios';
import PropTypes from "prop-types";
import { Container, Row, Col } from "shards-react";

import PageTitle from "../components/common/PageTitle";
import SmallStats from "../components/common/SmallStats";
import UsersOverview from "../components/DeliveryInfo/UsersOverview";
import DeliveryChart from "../components/DeliveryInfo/DeliveryChart";
import { Card, CardBody } from "shards-react";

const DeliveryOverview = ({ smallStats }) => {
  const [orderTimeDataText, setOrderTimeText] = useState("")
  const [orderTimeDataValue, setOrderTimeValue] = useState("")
  const [payAverageText, setPayAverageText] = useState("")
  const [payAverageValue, setPayAverageValue] = useState("")
  const [timeExpectText, setTimeExpectText] = useState("")
  const [timeExpectValue, setTimeExpectValue] = useState("")

  const smallst = [
    {
      label: orderTimeDataText,
      value: orderTimeDataValue+"건",
      chartLabels: [null, null, null, null, null, null, null],
      attrs: { md: "6", sm: "6" },
      datasets: [
        {
          label: "Today",
          fill: "start",
          borderWidth: 1.5,
          backgroundColor: "rgba(0, 184, 216, 0.1)",
          borderColor: "rgb(0, 184, 216)",
          data: [1, 2, 1, 3, 5, 4, 7]
        }
      ]
    },
    {
      label: payAverageText,
      value: payAverageValue+"원",
      percentage: "12.4",
      increase: true,
      chartLabels: [null, null, null, null, null, null, null],
      attrs: { md: "6", sm: "6" },
      datasets: [
        {
          label: "Today",
          fill: "start",
          borderWidth: 1.5,
          backgroundColor: "rgba(23,198,113,0.1)",
          borderColor: "rgb(23,198,113)",
          data: [1, 2, 3, 3, 3, 4, 4]
        }
      ]
    },
    {
      label: timeExpectText,
      value: timeExpectValue+"분",
      percentage: "3.8%",
      increase: false,
      decrease: true,
      chartLabels: [null, null, null, null, null, null, null],
      attrs: { md: "4", sm: "6" },
      datasets: [
        {
          label: "Today",
          fill: "start",
          borderWidth: 1.5,
          backgroundColor: "rgba(255,180,0,0.1)",
          borderColor: "rgb(255,180,0)",
          data: [2, 3, 3, 3, 4, 3, 3]
        }
      ]
    }
  ]
  
  const apiEndPoint = "https://64mg85mq2c.execute-api.us-east-1.amazonaws.com/hella/order";
  const getOrderTime = async () => {
      await axios.get(apiEndPoint).then((res) => {
          const data = res.data;

          setOrderTimeText(data['predict_order_text'])
          setOrderTimeValue(data['predict_order_value'])
          setPayAverageText(data['pay_avg_text'])
          setPayAverageValue(data['pay_avg_value'])
          setTimeExpectText(data['time_expect_text'])
          setTimeExpectValue(data['time_expect_value'])
      });
  };

  useEffect(() => {
      getOrderTime()
  }, []);

  return (
    <Container fluid className="main-content-container px-4">
      {/* Page Header */}
      <Row noGutters className="page-header py-4">
        <PageTitle title="HellaCles" subtitle="Hi Hella!" className="text-sm-left mb-3" />
      </Row>

      {/* Small Stats Blocks */}
      <Row>
        {smallst.map((stats, idx) => (
          <Col className="col-lg mb-4" key={idx} {...stats.attrs}>
            <SmallStats
              id={`small-stats-${idx}`}
              variation="1"
              chartData={stats.datasets}
              chartLabels={stats.chartLabels}
              label={stats.label}
              value={stats.value}
            />
          </Col>
        ))}
        <Col className="col-lg mb-4">
          <Card className="stats-small">
            <a href="https://hellaclestestb8d56c4974264760b616d2ac6c94bdf1151142-dev.s3.amazonaws.com/gangnamAlert.html">
              <h6 style={{fontWeight:"bold", textAlign:"center", margin:"40px", paddingTop:"10px"}}>강남구 동별 위험감지<br/>건수 확인</h6>
            </a>
            
          </Card>
        </Col>
      </Row>

      <Row>
        {/* Users Overview */}
        <Col lg="8" md="12" sm="12" className="mb-4">
          <UsersOverview />
        </Col>

        {/* Users by Device */}
        <Col lg="4" md="6" sm="12" className="mb-4">
          <DeliveryChart />
        </Col>
      </Row>
    </Container>
  )


};

DeliveryOverview.propTypes = {
  /**
   * The small stats dataset.
   */
  smallStats: PropTypes.array
};

DeliveryOverview.defaultProps = {
  smallStats: [
    {
      label: "12시 강남구 예상 주문 건수",
      value: "2,390",
      percentage: "4.7%",
      increase: true,
      chartLabels: [null, null, null, null, null, null, null],
      attrs: { md: "6", sm: "6" },
      datasets: [
        {
          label: "Today",
          fill: "start",
          borderWidth: 1.5,
          backgroundColor: "rgba(0, 184, 216, 0.1)",
          borderColor: "rgb(0, 184, 216)",
          data: [1, 2, 1, 3, 5, 4, 7]
        }
      ]
    }
  ]
};

export default DeliveryOverview;
